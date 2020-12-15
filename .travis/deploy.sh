# Inputs
FOLDER=$1
CLIENT=$2
URL=$3

# rsync flags used:
# -a: preserve attributes
# -v: verbose
# -u: updates only
# --delete: remove files not present in /tmp/FOLDER

# Sync $FOLDER with /tmp/$FOLDER
mkdir /tmp/$FOLDER && rsync -av $FOLDER/ /tmp/$FOLDER

# Checkout branch or create if not exists
git checkout $CLIENT || git checkout -b $CLIENT empty

# Sync files back to branch
rsync -avu --delete --exclude ".git" --exclude ".well-known" --exclude "netlify.toml" "/tmp/$FOLDER/" "."

# Copy public key if not present
if [ ! -f "./.well-known/amphtml/apikey.pub" ]; then
    mkdir -p .well-known/amphtml
    cp /tmp/apikey.pub .well-known/amphtml/
fi

# Copy netlify.toml and add redirect URL if not present
if [ ! -f "netlify.toml" ]; then
    cp /tmp/default.toml ./netlify.toml
    sed -i "s/###REDIRECT_URL###/$URL/g" netlify.toml
fi

# Add all files to new commit
git add *
git add .well-known

# Commit files to production branch
git commit -m "Travis build: $TRAVIS_BUILD_NUMBER"

# Push commit to repo
git push production $CLIENT
