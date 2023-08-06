from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.urls import reverse
from django.views import generic
from weasyprint import HTML

from huscy.consents.models import Consent
from huscy.consents.forms import SignatureForm
from huscy.consents.views import CreateConsentView, SignConsentView
from huscy.project_consents.forms import TokenForm
from huscy.project_consents.models import ProjectConsent, ProjectConsentFile, ProjectConsentToken
from huscy.projects.models import Project


class CreateProjectConsentView(CreateConsentView):

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        return super().dispatch(request, *args, **kwargs)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        response = super().post(self, request, *args, **kwargs)
        consent = Consent.objects.latest('id')
        ProjectConsent.objects.create(consent=consent, project=self.project)
        return response

    def get_success_url(self):
        return reverse('consent-created')


class CreateTokenView(generic.FormView):
    form_class = TokenForm
    template_name = 'project_consents/projectconsenttoken.html'

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def form_valid(self, form):
        token, _created = ProjectConsentToken.objects.get_or_create(
            created_by=self.request.user,
            project=form.cleaned_data.get('project'),
            subject=form.cleaned_data.get('subject'),
        )
        return HttpResponseRedirect(
            '{}?token={}'.format(reverse('create-project-consent-token'), token.id)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'token' in self.request.GET:
            token = get_object_or_404(ProjectConsentToken, pk=self.request.GET.get('token'))
            context['sign_project_consent_url'] = '{protocol}://{host}{url}'.format(
                protocol=self.request.scheme,
                host=self.request.get_host(),
                url=reverse('sign-project-consent', kwargs=dict(token=token.id))
            )
        return context


class SignProjectConsentView(SignConsentView):
    form_class = formset_factory(SignatureForm, extra=2)
    template_name = 'project_consents/sign_project_consent.html'

    def dispatch(self, request, *args, **kwargs):
        self.token = get_object_or_404(ProjectConsentToken, pk=self.kwargs['token'])
        self.consent = self.token.project.projectconsent.consent  # required by parent class
        return super(SignConsentView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experimenter'] = self.token.created_by
        context['project'] = self.token.project
        context['subject'] = self.token.subject
        return context

    def form_valid(self, form):
        html_template = get_template('project_consents/signed_project_consent.html')

        custom_data = dict((key, value)
                           for key, value in self.request.POST.items()
                           if key.startswith('textfragment'))
        rendered_html = html_template.render({
            'consent': self.consent,
            'custom_data': custom_data,
            'experimenter': self.token.created_by,
            'form': form,
            'subject': self.token.subject,
        })
        content = HTML(string=rendered_html, base_url=self.request.build_absolute_uri()).write_pdf()
        filehandle = SimpleUploadedFile(
            name='filehandle',
            content=content,
            content_type='application/pdf'
        )
        ProjectConsentFile.objects.create(
            consent_version=self.consent.version,
            filehandle=filehandle,
            project_consent=self.token.project.projectconsent,
            subject=self.token.subject
        )
        self.token.delete()
        return HttpResponse(content, content_type="application/pdf")
