import os

def main():
    folder_list = []
    with open('/tmp/updates', 'r') as diff_list:
        folder_list = [f for f in diff_list.readlines() if '/' in f and f[0] != '.']

    for folder in folder_list:
        client = folder[:folder.rfind('-')]
        url = folder[:folder.rfind('-')] + '.' + folder[folder.rfind('-') + 1:]

        os.system('.travis/deploy.sh %s %s %s' % (folder, client, url))

if __name__ == '__main__':
    main()