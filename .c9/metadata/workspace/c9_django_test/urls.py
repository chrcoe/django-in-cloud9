{"filter":false,"title":"urls.py","tooltip":"/c9_django_test/urls.py","undoManager":{"mark":52,"position":52,"stack":[[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":11,"column":1},"end":{"row":11,"column":67}},"text":" + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":0},"end":{"row":5,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":0},"end":{"row":5,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":5,"column":0},"end":{"row":5,"column":32}},"text":"from django.conf import settings"},{"action":"insertText","range":{"start":{"row":5,"column":32},"end":{"row":6,"column":0}},"text":"\n"},{"action":"insertText","range":{"start":{"row":6,"column":0},"end":{"row":6,"column":42}},"text":"from django.conf.urls.static import static"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":12,"column":0},"end":{"row":12,"column":39}},"text":"url(r'^polls/', include('polls.urls')),"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":12,"column":0},"end":{"row":12,"column":4}},"text":"    "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":14,"column":1},"end":{"row":14,"column":67}},"text":" + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":0,"column":0},"end":{"row":15,"column":0}},"nl":"\n","lines":["from django.conf.urls import patterns, include, url","","from django.contrib import admin","admin.autodiscover()","","from django.conf import settings","from django.conf.urls.static import static","","urlpatterns = patterns('',","    # Examples:","    # url(r'^$', 'c9_django_test.views.home', name='home'),","    # url(r'^blog/', include('blog.urls')),","    url(r'^polls/', include('polls.urls')),","    url(r'^admin/', include(admin.site.urls)),",")"]},{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":0,"column":51}},"text":"from django.conf.urls import patterns, include, url"},{"action":"insertText","range":{"start":{"row":0,"column":51},"end":{"row":1,"column":0}},"text":"\n"},{"action":"insertLines","range":{"start":{"row":1,"column":0},"end":{"row":8,"column":0}},"lines":["","from django.contrib import admin","admin.autodiscover()","","urlpatterns = patterns('',","    url(r'^polls/', include('polls.urls')),","    url(r'^admin/', include(admin.site.urls)),"]},{"action":"insertText","range":{"start":{"row":8,"column":0},"end":{"row":8,"column":1}},"text":")"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":8,"column":1},"end":{"row":8,"column":2}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":8,"column":2},"end":{"row":8,"column":3}},"text":"+"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":8,"column":3},"end":{"row":8,"column":4}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":8,"column":3},"end":{"row":8,"column":4}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":8,"column":2},"end":{"row":8,"column":3}},"text":"+"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":8,"column":2},"end":{"row":8,"column":67}},"text":"+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":1,"column":0},"end":{"row":1,"column":42}},"text":"from django.conf.urls.static import static"}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":1,"column":0},"end":{"row":2,"column":0}},"nl":"\n","lines":["from django.conf.urls.static import static"]},{"action":"insertLines","range":{"start":{"row":2,"column":0},"end":{"row":3,"column":0}},"lines":["from django.conf.urls.static import static"]}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":2,"column":0},"end":{"row":3,"column":0}},"nl":"\n","lines":["from django.conf.urls.static import static"]},{"action":"insertLines","range":{"start":{"row":3,"column":0},"end":{"row":4,"column":0}},"lines":["from django.conf.urls.static import static"]}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":42},"end":{"row":4,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":0},"end":{"row":4,"column":1}},"text":"f"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":1},"end":{"row":4,"column":2}},"text":"r"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":2},"end":{"row":4,"column":3}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":3},"end":{"row":4,"column":4}},"text":"m"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":4},"end":{"row":4,"column":5}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":4,"column":4},"end":{"row":4,"column":5}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":4,"column":3},"end":{"row":4,"column":4}},"text":"m"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":4,"column":2},"end":{"row":4,"column":3}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":4,"column":1},"end":{"row":4,"column":2}},"text":"r"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":4,"column":0},"end":{"row":4,"column":1}},"text":"f"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":0},"end":{"row":4,"column":1}},"text":"f"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":1},"end":{"row":4,"column":2}},"text":"r"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":2},"end":{"row":4,"column":3}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":3},"end":{"row":4,"column":4}},"text":"m"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":4},"end":{"row":4,"column":5}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":5},"end":{"row":4,"column":6}},"text":"c"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":6},"end":{"row":4,"column":7}},"text":"9"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":4,"column":5},"end":{"row":4,"column":7}},"text":"c9"},{"action":"insertText","range":{"start":{"row":4,"column":5},"end":{"row":4,"column":19}},"text":"c9_django_test"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":19},"end":{"row":4,"column":20}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":20},"end":{"row":4,"column":21}},"text":"i"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":21},"end":{"row":4,"column":22}},"text":"m"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":22},"end":{"row":4,"column":23}},"text":"p"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":23},"end":{"row":4,"column":24}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":24},"end":{"row":4,"column":25}},"text":"r"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":25},"end":{"row":4,"column":26}},"text":"t"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":26},"end":{"row":4,"column":27}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":27},"end":{"row":4,"column":28}},"text":"s"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":4,"column":28},"end":{"row":4,"column":29}},"text":"e"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":4,"column":27},"end":{"row":4,"column":29}},"text":"se"},{"action":"insertText","range":{"start":{"row":4,"column":27},"end":{"row":4,"column":35}},"text":"settings"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":9,"column":2},"end":{"row":9,"column":67}},"text":"+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":9,"column":1},"end":{"row":9,"column":2}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":4,"column":0},"end":{"row":4,"column":35}},"text":"from c9_django_test import settings"},{"action":"removeLines","range":{"start":{"row":3,"column":0},"end":{"row":4,"column":0}},"nl":"\n","lines":["from django.conf.urls.static import static"]},{"action":"removeText","range":{"start":{"row":2,"column":20},"end":{"row":3,"column":0}},"text":"\n"},{"action":"insertText","range":{"start":{"row":2,"column":20},"end":{"row":3,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":0},"end":{"row":4,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":3,"column":0},"end":{"row":4,"column":0}},"nl":"\n","lines":[""]}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":2,"column":20},"end":{"row":3,"column":0}},"text":"\n"}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":2,"column":20},"end":{"row":2,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1412040719275,"hash":"2afbf3484746398ef3b068f34d15c44698d32c22"}