# word-battle-game-2
Attempt 2 with cloud run and firestore

## Setting Up Environment Variables

This project requires a `.env` file to store sensitive credentials and configuration values. Follow the steps below to create and configure the `.env` file:

### 1. Create a `.env` File
In the root directory of the project, create a file named `.env`.

### 2. Add the Required Variables
Add the following key-value pairs to the `.env` file:

```
# Example .env file

FIREBASE_CREDENTIALS_JSON=creds/wordbattle-game-poc-firebase-adminsdk-fbsvc-82886dde08.json
```

### 3. Keep the `.json` Service Account file secure
- **Do not commit the `creds/*.json` file to version control.** Ensure it is listed in your `.gitignore` file.
- Share the `.json` file securely with team members who need access.

### 4. Loading the `.env` File
This project uses a library like `dotenv` to load environment variables from the `.env` file. Ensure the library is installed and properly configured in the project.

For example, in a Node.js project:
```javascript
require('dotenv').config();
```
