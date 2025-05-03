# Copy service account key from Downloads to current directory
cp ~/Downloads/wordbattle-game-poc-e202038a0522.json .

# List current directory contents
ls

# Create initial project folder structure
mkdir app
cd app
mkdir routes
mkdir utils
touch firestore.py

# (VSCode internal) Export environment variables to file [automated or extension-related]
# Skipping actual path as it's system-specific and not usually manually run:
# /usr/bin/python3 ... printEnvVariablesToFile.py ...

# Go back to project root
cd ..

# Activate Python virtual environment
source venv/bin/activate

# Run FastAPI app with Uvicorn in dev mode (hot reload)
uvicorn app.main:app --reload

# Run a test script to verify Firestore or other setup
python test_write.py

# Backup credentials folder with timestamp and unset GCP credentials
mv creds/ wordbattle-old-creds-backup-$(date +%Y%m%d%H%M)
unset GOOGLE_APPLICATION_CREDENTIALS

# Re-run test to check updated credentials or environment
python test_write.py

# Restart development server
uvicorn app.main:app --reload

# (VSCode internal) Another env var export, can be ignored for documentation purposes