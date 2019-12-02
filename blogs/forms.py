from django import forms
from blogs.models import Blog, Comment

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'article']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'article':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

    def save(self, user=None):
        blog_creator = super(BlogForm, self).save(commit=False)
        if user:
            blog_creator.author = user
        blog_creator.save()
        return blog_creator

    def user_privileges(self, user=None):
        blog_editor = super(BlogForm, self).save(commit=False)
        if user:
            if blog_editor.author == user:
                blog_editor.save()
                return True
            else:
                return False



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_text']

        widgets = {
            'comment_text':forms.Textarea(attrs={'class':'form-control'})
        }

    def save(self, user=None, blogID=None):
        comment_creator = super(CommentForm, self).save(commit=False)
        if user:
            comment_creator.author = user
        if blogID:
            comment_creator.blog_id = blogID
        comment_creator.save()
        return comment_creator


    def user_privileges(self, user=None):
        comment_editor = super(CommentForm, self).save(commit=False)
        if user:
            if comment_editor.author == user:
                comment_editor.save()
                return True
            else:
                return False

