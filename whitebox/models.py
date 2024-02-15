from django.db import models

class App(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    degree=models.CharField(
        max_length=100,
        choices=(('0','0%'),('10','10%'),("20","20%"),("30","30%"),
        ("40","40%"),("50","50%"),("60","60%"),("70","70%"),("80","80%"),
        ("90","90%"),("100","100%"),("120","limit-break"),),
        null=True,
    )
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)

class Comment(models.Model):
    text=models.TextField()
    target=models.ForeignKey('App',on_delete=models.CASCADE,verbose_name='対象記事')
    created_at=models.DateTimeField('CreatedDate',auto_now=True)
    username=models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='ユーザー名')

    def __str__(self):
        return self.text[:20]

    