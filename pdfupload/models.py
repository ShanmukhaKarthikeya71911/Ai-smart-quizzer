from django.db import models

# Create your models here.

from django.db import models

class UploadedPDF(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Uploaded PDF'
        verbose_name_plural = 'Uploaded PDFs'
        indexes = [
            models.Index(fields=['uploaded_at']),
        ]
    def delete(self, *args, **kwargs):
        self.file.delete(save=False)  # Delete the file from storage
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.file.name
        super().save(*args, **kwargs)