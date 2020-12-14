import os

def main():
    commit_message = os.getenv('TRAVIS_COMMIT_MESSAGE')

    os.system('git config --global user.email "travis@travis-ci.org"')
    os.system('git config --global user.name "Travis CI"')
    os.system('git remote add origin-production https://${GH_TOKEN}@github.com/gr0-autt/amp-production.git > /dev/null 2>&1')

    folder_list = commit_message.split(',')
    for folder in folder_list:
        client = folder[:folder.rfind('-')]
        url = folder[:folder.rfind('-')] + '.' + folder[folder.rfind('-') + 1:]

        os.system('mkdir /tmp/' + folder + ' && cp -r ' + folder + '/* /tmp/' + folder + '/')
        os.system('cp .skel/default.toml /tmp && cp .skel/apikey.pub /tmp')
        os.system('git checkout ' + client + ' || get checkout --orphan ' + client
        os.system('cp -r /tmp/' + folder + '/* .')
        os.system('mkdir .well-known && mkdir .well-known/amphtml && cp /tmp/apikey.pub .well-known/amphtml/')
        with open('/tmp/default.toml', 'r') as infile:
            with open('netlify.toml', 'w') as outfile:
                for line in infile:
                    outfile.write(line.replace('###REDIRECT_URL###', url))
        
        os.system('git add *')
        os.system('git commit -m "Travis build: ' + os.getenv('TRAVIS_BUILD_NUMBER'))
        os.system('git push --set-upstream origin-production ' + client)
        
    

if __name__ == '__main__':
    main()