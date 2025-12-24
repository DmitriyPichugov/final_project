import markdown
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "StroyBase - Главная"
        context["content"] = "Магазин стройматериалов StroyBase"
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "StroyBase - О нас"
        context["content"] = "О нас"
        markdown_text = """
        StroyBase — Ваш надежный партнер в мире строительных материалов

        Что мы предлагаем:

        - Широкий ассортимент товаров:  
        В нашем магазине вы найдете все необходимые строительные материалы — от цемента и кирпичей до высококачественных 
        отделочных материалов и оборудования. Мы уделяем особое внимание выбору товаров, чтобы обеспечить разнообразие для 
        различных проектов, включая как крупные строительные объекты, так и мелкий ремонт.

        - Гарантия качества:  
        Мы работаем только с надежными и проверенными брендами, которые зарекомендовали себя на рынке. Каждое изделие проходит 
        строгий контроль качества, что обеспечивает его долговечность и безопасность.

        - Консультации экспертов:  
        Наша команда готова предоставить профессиональные советы по выбору материалов, их применению, а также по оптимизации
        затрат на строительство и ремонт.

        - Доставка по всей России:  
        Независимо от того, где вы находитесь, мы обеспечим доставку в любой уголок страны. Для вашего удобства мы предлагаем
        разные варианты доставки — в том числе экспресс-доставку, если материалы необходимы срочно.

        - Ценовая политика:  
        Мы предлагаем конкурентоспособные цены, делая акцент на доступности качественных строительных материалов для всех
        клиентов.


        """
        
        html_content = markdown.markdown(markdown_text)
        context["text_on_page"] = html_content
        return context
