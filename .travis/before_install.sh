# Update repo to grab most recent git history
git fetch

# Pull empty repo to ensure new branches are created properly
git checkout origin/empty
git checkout origin/master

# Git user setup
git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

# Adding secondary remote for pushing using token
git remote add production https://${GH_TOKEN}@github.com/gr0-autt/amp-production.git > /dev/null 2>&1

# Write list of changed files to /tmp/updates
git diff --name-only ${TRAVIS_COMMIT}^..${TRAVIS_COMMIT} -- > /tmp/updates

# Copy skel files to /tmp
cp .skel/* /tmp/
