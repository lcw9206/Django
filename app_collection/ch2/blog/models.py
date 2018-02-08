from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique = True, allow_unicode= True, help_text = 'one word_for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    class Meta:
        verbose_name = 'post'           # 테이블의 단수 별칭을 post로 지정
        verbose_name_plural = 'posts'   # 테이블의 복수 별칭을 posts로 지정
        db_table = 'my_post'            # 테이블 이름을 my_post로 지정
        ordering = ('-modify_date',)    # 모델 객체의 리스트 출력 시, modify_date 컬럼을 기준으로 내림차순 정렬

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):                # modift_date 컬럼을 기준으로 이전 포스트를 반환
        return self.get_previous_by_modify_date()  # get_previous_modify_date는 내장함수

    def get_next_post(self):
        return self.get_next_by_modify_date()