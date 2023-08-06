import uuid

from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from huscy.consents.models import Consent, ConsentCategory, ConsentFile
from huscy.projects.models import Project
from huscy.subjects.models import Subject


class ProjectConsentCategory(models.Model):
    consent_category = models.OneToOneField(ConsentCategory, on_delete=models.PROTECT)

    @property
    def name(self):
        return self.consent_category.name

    @property
    def template_text_fragments(self):
        return self.consent_category.template_text_fragments


class ProjectConsentToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ProjectConsent(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    consent = models.ForeignKey(Consent, on_delete=models.PROTECT)

    @property
    def name(self):
        return self.consent.name

    @property
    def text_fragments(self):
        return self.consent.text_fragments


class ContactPerson(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)


def get_consent_file_upload_path(instance, filename):
    project_id = instance.project_consent.project.id
    subject_name = '_'.join(instance.subject.contact.display_name.lower().split())
    return f'projects/{project_id}/consents/{subject_name}'


class ProjectConsentFile(models.Model):
    project_consent = models.ForeignKey(ProjectConsent, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    consent_version = models.PositiveIntegerField(default=1)

    filehandle = models.FileField(upload_to=get_consent_file_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = 'project_consent', 'subject', 'consent_version'
