# -*- coding: utf-8 -*-

from django.http import JsonResponse
import re
from PIL import Image
from io import BytesIO
import requests
from bs4 import BeautifulSoup


def req(request):
    if request.POST:
        inf = dict()
        try:
            headers = {
                "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            }
            data = {'scripmanager1': 'pnlMain|btnSearch',
                    '__LASTFOCUS': '',
                    '__EVENTTARGET': 'btnSearch',
                    '__EVENTARGUMENT': '',
                    '__VIEWSTATE': 'EiYOve9Y/WgvPKGsG9J6zC41fW2xap9SIDuALyyr0mwu6x6qeP0xKWo7+jaR5IKf+oJG3qjtYl2GG0S29sffz0S/1cO+jGyQJY8KW6wA3vXAQTKmjFpn4lU1JfnpGYc1dHVVi/TLUXUVRwfVPiBJUlc+Uzvn+HX5/dqU7eUEXgs=',
                    '__VIEWSTATEGENERATOR': 'BBBC20B8',
                    '__VIEWSTATEENCRYPTED': '',
                    '__EVENTVALIDATION': 'YBHNJlgEDYi9rgOWFGvZDcCtE2v7LP67TACQBrY5zaXTC/y7r1tWrJnt8iKGVzXddx+9FpTxx4+SRZ3N7Nk7TMro/JoEJIqj+AinYlxZ0hTGktuAbd8Dk/GmbyGdg8atoBwlhzRyVnGvWSr9J/L2MVqA7ETGsqdCdrRnwuYTFa0=',
                    'txtbSearch': str(request.POST['number']),
                    '__ASYNCPOST': 'true',
                    }

            result = requests.post("https://newtracking.post.ir/", data=data, headers=headers)
            soup = BeautifulSoup(result.content, 'html.parser')

            inf["consignment_number"] = re.findall('>.*<', str(soup.find('span', id='lblParcel1')))[0].replace('<',
                                                                                                               '').replace(
                '>', '')
            inf["accepted_date"] = re.findall('>.*<', str(soup.find('span', id='lblParcelDate1')))[0].replace('<',
                                                                                                              '').replace(
                '>', '')
            inf['service_type'] = re.findall('>.*<', str(soup.find('span', id='lblParcelType')))[0].replace('<',
                                                                                                            '').replace(
                '>', '')
            inf['post_office_origin'] = re.findall('>.*<', str(soup.find('span', id='lblParcelSource')))[0].replace('<',
                                                                                                                    '').replace(
                '>', '')
            inf['origin'] = re.findall('>.*<', str(soup.find('span', id='lblSource')))[0].replace('<', '').replace('>',
                                                                                                                   '')
            inf['Destination'] = re.findall('>.*<', str(soup.find('span', id='lblDestination')))[0].replace('<',
                                                                                                            '').replace(
                '>', '')
            inf['sender'] = re.findall('>.*<', str(soup.find('span', id='lblParcelSender')))[0].replace('<',
                                                                                                        '').replace(
                '>',
                '')
            inf['reciver'] = re.findall('>.*<', str(soup.find('span', id='lblParcelReciver')))[0].replace('<',
                                                                                                          '').replace(
                '>',
                '')
            inf['sender_postal_code'] = re.findall('>.*<', str(soup.find('span', id='lblSPostalCode')))[0].replace('<',
                                                                                                                   '').replace(
                '>', '')
            inf['reciver_postal_code'] = re.findall('>.*<', str(soup.find('span', id='lblRPostalCode')))[0].replace('<',
                                                                                                                    '').replace(
                '>', '')
            inf['weight'] = re.findall('>.*<', str(soup.find('span', id='lblWeight')))[0].replace('<', '').replace('>',
                                                                                                                   '')
            inf['insurance_cost'] = re.findall('>.*<', str(soup.find('span', id='lblInsurance')))[0].replace('<',
                                                                                                             '').replace(
                '>', '')

            inf['consignment_inf'] = re.findall('>.*<', str(soup.find('span', id='lblParcelDescription')))[0].replace(
                '<',
                '').replace(
                '>', '')

            inf['postal_cost'] = re.findall(
                '<span id="lblPay">.*?<label id="lblmoredetail" onclick="ShowDetail',
                result.text)[0].replace('<span id="lblPay">', '').replace(
                '<label id="lblmoredetail" onclick="ShowDetail',
                '')

            date_time = re.findall(
                '<div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span>تاریخ و ساعت :</span><span>.*?</span></div>',
                result.text)[0].replace(
                '<div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span>تاریخ و ساعت :</span><span>',
                '').replace('</span></div>', '')
            post_city = re.findall(
                '<div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span>نقطه پستی : </span><span>.*?</span></div>',
                result.text)[0].replace(
                '<div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span>نقطه پستی : </span><span>',
                '').replace('</span></div>', '')

            postman = re.findall(
                '<div class="row"><div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span> نامه رسان : </span><span>.*?</span></div></div>',
                result.text)[0].replace(
                '<div class="row"><div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span> نامه رسان : </span><span>',
                '').replace('</span></div></div>', '')

            result_post = re.findall(
                '<b> نتيجه : </b><label style="color:green;">.*?</label></span></div>',
                result.text)[0].replace('<b> نتيجه : </b><label style="color:green;">', '').replace(
                '.</label></span></div>',
                '')

            function = re.findall(
                '<div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span>رویداد : </span><span>.*?<b>',
                result.text)[0].replace(
                '<div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span>رویداد : </span><span>',
                '').replace('.<b>', '')

            last_change = {'date_time': date_time, 'post_city': post_city, 'postman': postman,
                           'result_post': result_post,
                           'function': function}
            inf['last_change'] = last_change
            picture = "https://newtracking.post.ir" + re.findall('<img alt="نامه رسان" class="postmanimg" src=".*?"/>',
                                                                 str(soup.find_all('img', alt="نامه رسان")[1]))[
                0].replace(
                '<img alt="نامه رسان" class="postmanimg" src="', '').replace('"/>', '').replace('amp;', '')

            img = requests.get(picture, timeout=2)
            image = Image.open(BytesIO(img.content))
            inf['picture'] = str(image.tobytes())

            content = "<html><body>" + str(soup.find('div', id='trackdetail')) + "</body></html>"
            soup2 = BeautifulSoup(content, 'html.parser')
            tarikhs = soup2.findAll('div', attrs={"class": 'col-lg-2'})
            tarikhs = tarikhs[:len(tarikhs) - 1]
            for i in range(len(tarikhs)):
                tarikhs[i] = str(tarikhs[i]).replace('<div class="col-lg-2">', '').replace('</div>', '')
            logs = soup2.findAll('div', attrs={"class": 'col-lg-12'})
            logs = logs[:len(logs) - 3]
            log_lines = list()
            i = 3
            j = 0
            k = 0
            obj = list()
            obj.append(tarikhs[k])
            k += 1
            for log in logs:
                if 'class="lbl"' in str(log):
                    log_lines.append(re.findall(
                        '<div class="col-lg-12"><span class="lbl"><i class="fa fa-arrow-down"></i>.*?<i class="fa fa-arrow-down"></i></span></div>',
                        str(log))[0].replace(
                        '<div class="col-lg-12"><span class="lbl"><i class="fa fa-arrow-down"></i>',
                        '').replace('<i class="fa fa-arrow-down"></i></span></div>', ''))
                elif 'class="lbl2"' in str(log):
                    j += 1

                    obj.append(re.findall(
                        '<div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span>.*?</span><span>.*?</span></div>',
                        str(log))[0].replace(
                        '<div class="col-lg-12"><span class="lbl2"><span class="fa fa-arrow-circle-left" style="margin-left:5px;"></span>',
                        '').replace('</span><span>', '').replace('</span></div>', ''))
                    if i == j:
                        log_lines.append(obj)
                        obj = list()
                        obj.append(tarikhs[k])
                        k += 1
                        j = 0
                        if i == 3:
                            i = 2
                        elif i == 2:
                            i = 3

            log_lines = log_lines[:len(log_lines)]
            inf['log_lines'] = log_lines
            inf['error'] = "null"
        except Exception as e:
            inf.clear()
            inf['error'] = e.__str__()

        return JsonResponse(inf)


'189399816700021300068114'
'189399816700013320946114'
'189399816700014400795114'
