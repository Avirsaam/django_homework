from django.http import HttpResponse
from random import choice, randint
import logging

logger = logging.getLogger(__name__)

def index(request):
    html = """
        <!DOCTYPE html>
        <head>
            <title>HTML and CSS "Hello World"</title>
            <style>
                body {
                    background-color: #2D2D2D;
                }                
                h1 {
                    color: #C26356;
                    font-size: 30px;
                    font-family: Menlo, Monaco, fixed-width;
                }                
                p {
                    color: white;
                    font-family: "Source Code Pro", Menlo, Monaco, fixed-width;
                }
            </style>
        </head>
        <body>
            <h1>Домащняя работа номер 1</h1>
            <p>Простой пример страницы</p>
        </body>
        </html>
        """
    logger.debug(f'index page assessed by {request.get_host()}')
    return HttpResponse(html)

def about(request):
    html = """
        <!DOCTYPE html>
        <head>
            <title>About</title>
            <style>
                body {
                    background-color: lightgray;
                }                
                h1 {
                    color: #C26356;
                    font-size: 30px;
                    font-family: Menlo, Monaco, fixed-width;
                }                
                p {
                    color: #40A7E3;
                    font-family: "Source Code Pro", Menlo, Monaco, fixed-width;
                }
            </style>
        </head>
        <body>
            <h1>Страница About</h1>
            <p>Elit velit magna ea id deserunt mollit aute voluptate aliqua. Qui proident velit excepteur officia et deserunt. Eiusmod eiusmod aute et exercitation.</p>
            <p>Culpa dolore proident elit Lorem sint minim adipisicing dolor ullamco laborum ex. Quis eiusmod excepteur ullamco aliquip irure. Esse nisi anim pariatur fugiat incididunt tempor exercitation quis proident. Officia amet nisi pariatur laboris sunt sit ipsum aliquip. Ad est sint elit reprehenderit proident. Lorem id aliquip duis minim cupidatat deserunt anim aliqua. Duis consectetur excepteur pariatur ullamco in officia irure.</p>
        </body>
        </html>
        """
    logger.debug(f'"about" page assessed by {request.get_host()}')
    return HttpResponse(html)

