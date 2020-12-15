echo ${TRAVIS_COMMIT_RANGE}

git fetch
git checkout origin/empty
git checkout origin/master
git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"
git remote add production https://${GH_TOKEN}@github.com/gr0-autt/amp-production.git > /dev/null 2>&1
