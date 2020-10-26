import os
import argparse
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--client')
    parser.add_argument('-i')
    parser.add_argument('--user')
    args = parser.parse_args()

    dest_folder = './' + args.client

    os.system('mkdir ' + args.client)  # make client directory
    os.system(r'scp -i ' + args.i + ' ' + args.user + '@34.73.69.180:/var/www/html/' + args.client + r'/\*.html ' + dest_folder)  # pull all files from server

    ignore_files = [
        '_0.1.pre.html',
        '_1.pre.html',
        '_1.0.pre.html',
        '_1.1.0.pre.html',
        '_1.1.pre.html',
        '_1.2.pre.html',
        '_1.3.pre.html',
        '_1.4.pre.html',
        '_2.pre.html',
        '_3.pre.html',
        '_3.1.pre.html',
        '_4.pre.html',
        '_5.pre.html',
        '_6.pre.html',
        '_7.pre.html',
        '_8.pre.html',
        '_9.pre.html',
        '_10.pre.html',
        '_10.1.pre.html',
        '_10.2.pre.html',
        '_11.pre.html',
        '_13.pre.html',
        '_14.pre.html',
        '_14.2.pre.html',
        '_14.2.0.pre.html',
        '_14.2.1.pre.html',
        '_14.3.pre.html',
        '_14.4.pre.html',
        '_14.5.pre.html',
        '_14.6.pre.html',
        '_14.7.pre.html',
        '_14.8.pre.html',
        '_14.9.pre.html',
        '_15.pre.html',
        '_16.pre.html',
        '_16.0.pre.html',
        '_16.1.pre.html',
        '_16.2.pre.html',
        '_16.3.pre.html',
        '_16.4.pre.html',
        '_16.5.pre.html',
        '_16.6.pre.html',
        '_16.7.pre.html',
        '_16.8.pre.html',
        '_16.9.pre.html',
        '_16.10.pre.html',
        '_16.11.pre.html',
        '_16.12.pre.html',
        '_16.13.pre.html',
        '_16.14.pre.html',
        '_16.15.pre.html',
        '_16.16.pre.html',
        '_16.17.pre.html',
        '_16.18.pre.html',
        '_16.19.pre.html',
        '_16.20.pre.html',
        '_16.21.pre.html',
        '_16.22.pre.html',
        '_16.23.pre.html',
        '_16.24.pre.html',
        '_16.25.pre.html',
        '_16.26.pre.html',
        '_16.27.pre.html',
        '_16.28.pre.html',
        '_16.29.pre.html',
        '_16.30.pre.html',
        '_16.31.pre.html',
        '_16.32.pre.html',
        '_17.pre.html',
        '_17.pre.html.1.html',
        '_18.pre.html',
        'combine.html',
        'main.html',
        'main.html.bs4.html',
        'main.html.stage.1.html',
        'main.html.stage.2.html',
        'main.image.reference.html',
        'main.orig.html',
        'main.reference.html',
        'original_page.html',
        'page.html',
        'page.html.html',
        'pup.pre.html',
        '_raw.html'
    ]

    files = [f for f in os.listdir(dest_folder) if os.path.isfile(os.path.join(dest_folder, f))]
    for f in files:
        if f in ignore_files:
            os.system('rm ' + os.path.join(dest_folder, f))
            continue

        html = open(os.path.join(dest_folder, f), 'r')
        soup = BeautifulSoup(html, 'html.parser')
        canonical_tag = soup.find('link', {'rel':'canonical'})
        if canonical_tag:
            url = canonical_tag['href']
            idx = -1
            for i in range(0, 3):
                idx = url.find('/', idx + 1)
            
            path = url[idx + 1:]
            idx = 1
            while True:
                idx = path.find('/', idx + 1)
                if idx == -1:
                    break
                if not os.path.exists(os.path.join(dest_folder, path[:idx])):
                    cmd = 'mkdir ' + os.path.join(dest_folder, path[:idx])
                    os.system(cmd)
            if '/' in path:
                to_remove = path[:path.rindex('/') + 1].replace('/','-')
            else:
                to_remove = ''
            mv_cmd = 'mv ' + os.path.join(dest_folder, f) + ' ' + os.path.join(dest_folder, (path[:path.rindex('/') + 1] if '/' in path else path) + f.replace(to_remove, ''))
            os.system(mv_cmd)

if __name__ == '__main__':
    main()
