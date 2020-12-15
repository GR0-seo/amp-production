import os

def main():
    commit_message = os.getenv('TRAVIS_COMMIT_MESSAGE')

    folder_list = commit_message.split(',')
    for folder in folder_list:
        client = folder[:folder.rfind('-')]
        url = folder[:folder.rfind('-')] + '.' + folder[folder.rfind('-') + 1:]

        cmd = 'mkdir /tmp/' + folder + ' && cp -r ' + folder + '/* /tmp/' + folder + '/'
        print(cmd)
        os.system(cmd)

        cmd = 'cp .skel/default.toml /tmp && cp .skel/apikey.pub /tmp'
        print(cmd)
        os.system(cmd)

        cmd = 'git checkout empty && git checkout master'
        print(cmd)
        os.system(cmd)

        cmd = 'git checkout ' + client + ' || git checkout -b ' + client + ' empty'
        print(cmd)
        os.system(cmd)

        cmd = 'cp -r /tmp/' + folder + '/* .'
        print(cmd)
        os.system(cmd)

        cmd = 'mkdir .well-known && mkdir .well-known/amphtml && cp /tmp/apikey.pub .well-known/amphtml/'
        print(cmd)
        os.system(cmd)

        with open('/tmp/default.toml', 'r') as infile:
            with open('netlify.toml', 'w') as outfile:
                for line in infile:
                    outfile.write(line.replace('###REDIRECT_URL###', url))
        
        cmd = 'git add *'
        print(cmd)
        os.system(cmd)

        cmd = 'git add .well-known'
        print(cmd)
        os.system(cmd)

        cmd = 'git commit -m "Travis build: ' + os.getenv('TRAVIS_BUILD_NUMBER') + '"'
        print(cmd)
        os.system(cmd)

        cmd = 'git push --set-upstream origin-production ' + client
        print(cmd)
        os.system(cmd)
        
    

if __name__ == '__main__':
    main()