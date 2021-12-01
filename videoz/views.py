from django.shortcuts import render
from .models import Item
from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

list_3 = ['https://youtube.com/watch?v=vQQEaSnQ_bs', 'https://youtube.com/watch?v=1KO_HZtHOWI', 'https://youtube.com/watch?v=coZbOM6E47I', 'https://youtube.com/watch?v=th5_9woFJmk', 'https://youtube.com/watch?v=RO6JxDOVwLQ', 'https://youtube.com/watch?v=N6hyN6BW6ao', 'https://youtube.com/watch?v=UFuo7EHI8zc', 'https://youtube.com/watch?v=KdmPHEnPJPs', 'https://youtube.com/watch?v=txMdrV1Ut64', 'https://youtube.com/watch?v=T11QYVfZoD0', 'https://youtube.com/watch?v=HQ6XO9eT-fc', 'https://youtube.com/watch?v=DCDe29sIKcE', 'https://youtube.com/watch?v=Lw2rlcxScZY', 'https://youtube.com/watch?v=W9XjRYFkkyw', 'https://youtube.com/watch?v=zmdjNSmRXF4', 'https://youtube.com/watch?v=ZyhVh-qRZPA', 'https://youtube.com/watch?v=z0gguhEmWiY', 'https://youtube.com/watch?v=_P7X8tMplsw', 'https://youtube.com/watch?v=fKl2JW_qrso', 'https://youtube.com/watch?v=IEEhzQoKtQU', 'https://youtube.com/watch?v=mO_dS3rXDIs', 'https://youtube.com/watch?v=2Fp1N6dof0Y', 'https://youtube.com/watch?v=-nh9rCzPJ20', 'https://youtube.com/watch?v=06I63_p-2A4', 'https://youtube.com/watch?v=_JGmemuINww', 'https://youtube.com/watch?v=zdJEYhA2AZQ', 'https://youtube.com/watch?v=1lxrb_ezP-g', 'https://youtube.com/watch?v=APOPm01BVrk', 'https://youtube.com/watch?v=Kg1Yvry_Ydk', 'https://youtube.com/watch?v=C-gEQdGVXbk', 'https://youtube.com/watch?v=JRCJ6RtE3xU', 'https://youtube.com/watch?v=a6fIbtFB46g', 'https://youtube.com/watch?v=yqm6MBt-yfY', 'https://youtube.com/watch?v=tb8gHvYlCFs', 'https://youtube.com/watch?v=6DI_7Zja8Zc', 'https://youtube.com/watch?v=6DI_7Zja8Zc', 'https://youtube.com/watch?v=kt3ZtW9MXhw', 'https://youtube.com/watch?v=kt3ZtW9MXhw', 'https://youtube.com/watch?v=NhidVhNHfeU', 'https://youtube.com/watch?v=NhidVhNHfeU', 'https://youtube.com/watch?v=Gdys9qPjuKs', 'https://youtube.com/watch?v=D2lwk1Ukgz0', 'https://youtube.com/watch?v=D2lwk1Ukgz0', 'https://youtube.com/watch?v=LUFn-QVcmB8', 'https://youtube.com/watch?v=goToXTC96Co', 'https://youtube.com/watch?v=Sa_kQheCnds', 'https://youtube.com/watch?v=Sa_kQheCnds', 'https://youtube.com/watch?v=Qu3dThVy6KQ', 'https://youtube.com/watch?v=C3Z9lJXI6Qw', 'https://youtube.com/watch?v=jTYiNjvnHZY', 'https://youtube.com/watch?v=zDYL22QNiWk', 'https://youtube.com/watch?v=-tyBEsHSv7w', 'https://youtube.com/watch?v=-tyBEsHSv7w', 'https://youtube.com/watch?v=acOktTcTVEQ', 'https://youtube.com/watch?v=acOktTcTVEQ', 'https://youtube.com/watch?v=-s7e_Fy6NRU', 'https://youtube.com/watch?v=-s7e_Fy6NRU', 'https://youtube.com/watch?v=CQ90L5jfldw', 'https://youtube.com/watch?v=CQ90L5jfldw', 'https://youtube.com/watch?v=FdVuKt_iuSI', 'https://youtube.com/watch?v=FdVuKt_iuSI', 'https://youtube.com/watch?v=3aVqWaLjqS4', 'https://youtube.com/watch?v=3aVqWaLjqS4', 'https://youtube.com/watch?v=q4jPR-M0TAQ', 'https://youtube.com/watch?v=q4jPR-M0TAQ', 'https://youtube.com/watch?v=aHC3uTkT9r8', 'https://youtube.com/watch?v=aHC3uTkT9r8', 'https://youtube.com/watch?v=1PkNiYlkkjo', 'https://youtube.com/watch?v=1PkNiYlkkjo', 'https://youtube.com/watch?v=qDwdMDQ8oX4', 'https://youtube.com/watch?v=qDwdMDQ8oX4', 'https://youtube.com/watch?v=a48xeeo5Vnk', 'https://youtube.com/watch?v=a48xeeo5Vnk', 'https://youtube.com/watch?v=UmljXZIypDc', 'https://youtube.com/watch?v=UmljXZIypDc', 'https://youtube.com/watch?v=OdIHeg4jj2c', 'https://youtube.com/watch?v=PUIE7CPANfo', 'https://youtube.com/watch?v=nghuHvKLhJA', 'https://youtube.com/watch?v=r3R3h5ly_8g', 'https://youtube.com/watch?v=uVNfQDohYNI', 'https://youtube.com/watch?v=Wfx4YBzg16s', 'https://youtube.com/watch?v=vutyTx7IaAI', 'https://youtube.com/watch?v=PSWf2TjTGNY', 'https://youtube.com/watch?v=u0oDDZrDz9U', 'https://youtube.com/watch?v=803Ei2Sq-Zs', 'https://youtube.com/watch?v=CSHx6eCkmv0', 'https://youtube.com/watch?v=44PvX0Yv368', 'https://youtube.com/watch?v=cYWiDiIUxQc', 'https://youtube.com/watch?v=UIJKdCIEXUQ', 'https://youtube.com/watch?v=QnDWIZuWYW0', 'https://youtube.com/watch?v=MwZwr5Tvyxo', 'https://youtube.com/watch?v=IolxqkL7cD8', 'https://youtube.com/watch?v=5iWhQWVXosU', 'https://youtube.com/watch?v=k8asfUbWbI4', 'https://youtube.com/watch?v=-aKFBoZpiqA', 'https://youtube.com/watch?v=9N6a-VLBa2I', 'https://youtube.com/watch?v=ng2o98k983k', 'https://youtube.com/watch?v=K8L6KVGG-7o', 'https://youtube.com/watch?v=cY2NXB_Tqq0', 'https://youtube.com/watch?v=KzqSDvzOFNA', 'https://youtube.com/watch?v=6tNS--WetLI', 'https://youtube.com/watch?v=q5uM4VKywbA', 'https://youtube.com/watch?v=bkpLhQd6YQM', 'https://youtube.com/watch?v=CqvZ3vGoGs0', 'https://youtube.com/watch?v=9Os0o3wzS_I', 'https://youtube.com/watch?v=6iF8Xb7Z3wQ', 'https://youtube.com/watch?v=DZwmZ8Usvnk', 'https://youtube.com/watch?v=daefaLgNkw0', 'https://youtube.com/watch?v=W8KRzm-HUcc', 'https://youtube.com/watch?v=khKv-8q7YmY', 'https://youtube.com/watch?v=k9TUPpGqYTo', 'https://youtube.com/watch?v=YYXdXT2l-Gg', 'https://youtube.com/watch?v=pd-0G0MigUA', 'https://youtube.com/watch?v=KlBPCzcQNU8', 'https://youtube.com/watch?v=jxmzY9soFXg', 'https://youtube.com/watch?v=-ARI4Cz-awo', 'https://youtube.com/watch?v=xFciV6Ew5r4', 'https://youtube.com/watch?v=DjEuROpsvp4', 'https://youtube.com/watch?v=QVdf0LgmICw', 'https://youtube.com/watch?v=jCzT9XFZ5bw', 'https://youtube.com/watch?v=YJC6ldI3hWk', 'https://youtube.com/watch?v=3ohzBxoFHAY', 'https://youtube.com/watch?v=eirjjyP2qcQ', 'https://youtube.com/watch?v=RSl87lqOXDE', 'https://youtube.com/watch?v=rq8cL2XMM5M', 'https://youtube.com/watch?v=BJ-VvGyQxho', 'https://youtube.com/watch?v=ZDa-Z5JzLYM', 'https://youtube.com/watch?v=Uh2ebFW8OYM', 'https://youtube.com/watch?v=tJxcKyFMTGo', 'https://youtube.com/watch?v=FsAPt_9Bf3U', 'https://youtube.com/watch?v=vTX3IwquFkc', 'https://youtube.com/watch?v=xqcTfplzr7c', 'https://youtube.com/watch?v=x3v9zMX1s4s', 'https://youtube.com/watch?v=ve2pmm5JqmI', 'https://youtube.com/watch?v=D3JvDWO-BY4', 'https://youtube.com/watch?v=6Qs3wObeWwc', 'https://youtube.com/watch?v=NIWwJbo-9_8', 'https://youtube.com/watch?v=ajrtAuDg3yw', 'https://youtube.com/watch?v=NDFbXIiqT4o', 'https://youtube.com/watch?v=DEwgZNC-KyE', 'https://youtube.com/watch?v=3dt4OGnU5sM', 'https://youtube.com/watch?v=bD05uGo_sVI', 'https://youtube.com/watch?v=Dh-0lAyc3Bc', 'https://youtube.com/watch?v=GfxJYp9_nJA', 'https://youtube.com/watch?v=5cvM-crlDvg', 'https://youtube.com/watch?v=U2ZN104hIcc', 'https://youtube.com/watch?v=N5vscPTWKOk', 'https://youtube.com/watch?v=sugvnHA7ElY']
API_KEY = 'AIzaSyC_Fvhju-o30COmWETkjg8T2Ph8Tz2Q_IU'
CHANNEL_ID = 'UC8butISFwT-Wl7EV0hUK0BQ'
# Create your views here.
@login_required(login_url="accounts")

def show_videoz(request):
    # youtube = build('youtube', 'v3', developerKey=API_KEY)
    # res = youtube.channels().list(id=CHANNEL_ID, part='contentDetails').execute()
    # playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']    
    # videos = []
    # next_page_token = None
    
    # while 1:
    #     res = youtube.playlistItems().list(playlistId=playlist_id, 
    #                                        part='snippet', 
    #                                        maxResults=50,
    #                                        pageToken=next_page_token).execute()
    #     videos += res['items']
    #     next_page_token = res.get('nextPageToken')
        
    #     if next_page_token is None:
    #         break
    # prefer_list = ["Python", "Django", "Machine Learning", "Data Science"]
    # dict_1 = {}
    # for video in videos[:]:
    #     lis = video['snippet']['title'].split()
    #     for item in prefer_list:
    #         if item in lis:
    #             # print(type(video['snippet']['title']))
    #             dict_1[video['snippet']['title']] = ["https://youtube.com/watch?v=" + str(video['snippet']['resourceId']['videoId']), video['snippet']['thumbnails']['default']['url']]
    #             continue
    obj = Item.objects.all().order_by("?")[:]
    p = Paginator(obj,6)
    page = request.GET.get('page')
    chapter = p.get_page(page)
    return render(request, "videoz/videoz.html", {
        "chapter" : chapter
    })