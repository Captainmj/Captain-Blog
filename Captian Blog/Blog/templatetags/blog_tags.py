from django import template
from ..models import Article, Categroy
from django.utils.safestring import mark_safe        # 导入django内部安全方法
from django.db.models import Count                  
import markdown                                      # 导入markdown应用，使帖子可以使用markdown语法


register = template.Library()


@register.simple_tag
def get_recent_posts(num=3):
    return Article.objects.all()[:num]


#按日期归档自定义标签
@register.simple_tag
def archives():
    return Article.objects.dates('created', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Categroy.objects.all()


@register.filter(name='markdown')
#注册己的模板过滤器（template filter），过滤器（filter）命名为markdown
def markdown_format(text):
	#避免函数名和markdown模板名起冲突，将函数命名为markdown_format
    return mark_safe(markdown.markdown(text))
    '''使用Django提供的mark_safe方法来标记结果，在模板（template）中作为安全的HTML被渲染
    默认的，Django不会信赖任何HTML代码并且在输出之前会进行转义。唯一的例外就是被标记为安
    全转义的变量。这样的操作可以阻止Django从输出中执行潜在的危险的HTML，并且允许你创建一
    些例外情况只要你知道你正在运行的是安全的HTML。'''


#展示拥有最多评论的帖子
@register.assignment_tag
def get_most_commented_articles(count=3):
    return Article.objects.annotate(
                total_comments=Count('comments')
            ).order_by('-total_comments')[:count]