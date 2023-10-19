from django.db import models

class Archive(models.Model):
    archiveid = models.AutoField('ArchiveID', primary_key=True, unique=True)
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'アーカイブ'
        verbose_name_plural = 'アーカイブ'

class Movie(models.Model):
    archive = models.ForeignKey(Archive, on_delete=models.PROTECT, to_field='archiveid', related_name='movies')
    title = models.CharField(max_length=20)
    video = models.FileField(upload_to='movies/')
    
    def __str__(self):
        return str(self.archive)
    
    class Meta:
        verbose_name = '動画'
        verbose_name_plural = '動画'