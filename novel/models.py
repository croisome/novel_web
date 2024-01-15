from django.db import models


# Create your models here.


# genre of novel
class BookCategory(models.Model):
    work_direction = models.IntegerField(null=True)
    # name of genre
    name = models.CharField(null=True)
    sort = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class AuthorInfo(models.Model):
    user_id = models.BigIntegerField(null=True)
    invite_code = models.CharField(max_length=20)
    pen_name = models.CharField(max_length=20)
    # phone, email, qq, wechat
    chat_account = models.JSONField()
    work_direction = models.ForeignKey(BookCategory,
                                       on_delete=models.CASCADE,
                                       db_constraint=False)
    status = models.PositiveSmallIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class BookInfo(models.Model):
    # book genre in table category
    category_id = models.ForeignKey(BookCategory,
                                    on_delete=models.CASCADE,
                                    db_constraint=False,
                                    null=True)
    # book cover url
    pic_url = models.CharField(max_length=200,
                               null=True)
    book_name = models.CharField(max_length=50, )

    # id in author_info
    author_id = models.ForeignKey(AuthorInfo,
                                  on_delete=models.CASCADE,
                                  db_constraint=False,
                                  null=True)
    author_name = models.CharField(null=True, max_length=50)
    book_desc = models.CharField(null=True, max_length=200)
    score = models.PositiveSmallIntegerField(null=True)
    book_status = models.PositiveSmallIntegerField(null=True)
    visit_count = models.PositiveBigIntegerField(null=True)
    word_count = models.IntegerField(null=True)
    comment_count = models.IntegerField(null=True)
    last_chapter_id = models.PositiveBigIntegerField(null=True)
    last_chapter_name = models.CharField(null=True, max_length=50)
    last_chapter_update_time = models.DateTimeField(null=True)
    is_vip = models.PositiveSmallIntegerField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class BookChapter(models.Model):
    book_id = models.ForeignKey(BookInfo,
                                on_delete=models.CASCADE,
                                db_constraint=False)

    chapter_num = models.PositiveSmallIntegerField(null=True)
    chapter_name = models.CharField(null=True,
                                    max_length=50)
    word_count = models.PositiveIntegerField(null=True)
    is_vip = models.PositiveIntegerField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class BookContent(models.Model):
    chapter_id = models.ForeignKey(BookChapter, null=True,
                                   on_delete=models.CASCADE,
                                   db_constraint=False)
    content = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class BookComment(models.Model):
    book_id = models.ForeignKey(BookInfo,
                                null=True,
                                on_delete=models.CASCADE,
                                db_constraint=False)
    user_id = models.ForeignKey(AuthorInfo,
                                null=True,
                                db_constraint=False)
    comment_content = models.CharField(max_length=512)
    reply_count = models.PositiveIntegerField(null=True)
    # can express be deleted
    audit_status = models.PositiveSmallIntegerField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    next_comment_id = models.ForeignKey('self',
                                        on_delete=models.CASCADE,
                                        null=True,
                                        db_constraint=False)

    last_comment_id = models.ForeignKey('self',
                                        on_delete=models.CASCADE,
                                        null=True,
                                        db_constraint=False)