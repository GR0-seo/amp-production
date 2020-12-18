import os

def main():
    folder_list = []
    with open('/tmp/updates', 'r') as diff_list:
        file_list = [f for f in diff_list.readlines() if '/' in f and f[0] != '.']

    complete = []
    for file_ in file_list:
        folder = file_[:file_.find('/')]
        if folder in complete:
            continue
        
        client = folder[:folder.rfind('-')]
        url = folder[:folder.rfind('-')] + '.' + folder[folder.rfind('-') + 1:]

        os.system('.travis/deploy.sh %s %s %s' % (folder, client, url))

        complete.append(folder)

if __name__ == '__main__':
    main()