🧠  **Code Review Assistant**
<div align="center">
Intelligent AI-powered code reviewer that elevates your code quality through automated analysis
Built with FastAPI • React • Tailwind CSS • Powered by Advanced LLM Technology


</div>

🌟 What Makes This Special?
Code Review Assistant revolutionizes the way you approach code quality. No more waiting for peer reviews or second-guessing your implementation choices. Get instant, comprehensive feedback powered by cutting-edge AI technology.
💎 Key Highlights

🎯 Smart Analysis — Deep code understanding beyond simple linting
⚡ Instant Feedback — Get reviews in seconds, not hours
🎨 Beautiful Interface — Clean, modern UI that makes reviewing enjoyable
🔒 Privacy-First — Your code stays secure with optional local processing
📊 Actionable Insights — Not just problems, but solutions and best practices
🌐 Multi-Language Support — Works with Python, JavaScript, TypeScript, Java, and more


🎯 Features
🖥️ Backend Excellence (FastAPI)

🔌 RESTful API Architecture — Clean, well-documented endpoints
🤖 LLM Integration — Seamlessly connects with OpenAI, Anthropic, or local models
📦 Structured Responses — Consistent JSON format for easy parsing
💾 Persistent Storage — Optional database for review history and analytics
🔐 Secure File Handling — Validation and sanitization built-in
📈 Performance Optimized — Async operations for handling multiple requests

🎨 Frontend Beauty (React + Tailwind)

📤 Drag-and-Drop Upload — Intuitive file submission interface
🎭 Syntax Highlighting — View your code with proper formatting
📊 Visual Metrics Dashboard — Quality scores and trend analysis
🌓 Dark/Light Themes — Comfortable viewing in any environment
⚡ Real-time Updates — Live status of analysis progress
📱 Fully Responsive — Perfect experience on desktop, tablet, and mobile
♿ Accessibility First — WCAG compliant design

📋 Comprehensive AI Review Report
📝 Code Quality Summary
├─ 🎯 Overall Score (0-100)
├─ 📖 Readability Analysis
├─ ⚡ Performance Insights
├─ 🛡️ Security Vulnerabilities
├─ 🧩 Architecture Review
├─ 🎨 Code Style Compliance
├─ 🐛 Bug Detection
└─ 💡 Refactoring Suggestions
Each issue includes:

📍 Exact line numbers and code snippets
🚦 Severity level (Critical, High, Medium, Low)
💬 Clear explanation of the problem
✨ Suggested fixes with code examples
🔗 Links to relevant documentation


🏗️ Tech Stack
<div align="center">
LayerTechnologyPurpose🎨 FrontendReact 18, Tailwind CSS v4Modern, responsive UI⚙️ BackendFastAPI, Python 3.10+, UvicornHigh-performance API server🤖 AI EngineOpenAI GPT-4 / Anthropic ClaudeIntelligent code analysis💾 DatabaseSQLite / PostgreSQL (optional)Review history & analytics🔍 Code AnalysisTree-sitter, AST parsingSyntax understanding🧪 TestingPytest, React Testing LibraryQuality assurance📦 DeploymentDocker, Docker ComposeEasy containerization🔄 Version ControlGit, GitHub ActionsCI/CD pipeline
</div>

⚙️ Installation & Setup
📋 Prerequisites

Python 3.10 or higher
Node.js 18.x or higher
npm or yarn package manager
API Key from OpenAI/Anthropic (or use local LLM)

🔹 Quick Start (5 minutes)
1️⃣ Clone the Repository
bashgit clone https://github.com/supriyabaghel/code-review-assistant.git
cd code-review-assistant
2️⃣ Backend Setup
bash# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your API keys

# Run the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
3️⃣ Frontend Setup
bash# Open new terminal, navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

#### 4️⃣ Access the Application
```
🌐 Frontend: http://localhost:5173
📡 Backend API: http://localhost:8000
📚 API Docs: http://localhost:8000/docs
🐳 Docker Deployment (Recommended)
bash# Build and run with Docker Compose
docker-compose up -d

# Application will be available at http://localhost:3000

📖 Usage Guide
📤 Upload Code for Review

Select File — Click or drag-and-drop your code file (.py, .js, .ts, .java, etc.)
Configure Options — Choose review depth and focus areas
Submit — Click "Analyze Code"
Review Results — Explore findings categorized by severity
Export Report — Download as PDF, Markdown, or JSON

🔧 API Integration
bash# Example: Review code via curl
curl -X POST "http://localhost:8000/api/review" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_code.py" \
  -F "language=python"
python# Example: Python client
import requests

with open("your_code.py", "rb") as f:
    response = requests.post(
        "http://localhost:8000/api/review",
        files={"file": f},
        data={"language": "python"}
    )
    
review = response.json()
print(f"Overall Score: {review['score']}/100")

📊 Configuration
Environment Variables
env# Backend (.env)
OPENAI_API_KEY=your_openai_key_here
MODEL_NAME=gpt-4-turbo-preview
MAX_FILE_SIZE=5242880  # 5MB in bytes
ALLOWED_LANGUAGES=python,javascript,typescript,java,go
DATABASE_URL=sqlite:///./reviews.db

# Frontend (.env.local)
VITE_API_BASE_URL=http://localhost:8000
VITE_MAX_FILE_SIZE=5



🗺️ Roadmap

 Core review functionality
 Multi-language support
 Beautiful UI/UX
 VS Code Extension (Coming Soon)
 GitHub Action Integration — Auto-review PRs
 Team Analytics Dashboard — Track code quality over time
 Custom Rule Engine — Define your own review criteria
 Batch Processing — Review entire repositories
 Comparison Mode — Before/after refactoring analysis


🤝 Contributing
We welcome contributions! Whether it's bug fixes, feature additions, or documentation improvements.
How to Contribute

🍴 Fork the repository
🌿 Create a feature branch (git checkout -b feature/AmazingFeature)
💾 Commit changes (git commit -m 'Add some AmazingFeature')
📤 Push to branch (git push origin feature/AmazingFeature)
🔃 Open a Pull Request

See CONTRIBUTING.md for detailed guidelines.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments

OpenAI for GPT-4 API access
FastAPI team for the excellent framework
React and Tailwind communities for amazing tools


📬 Contact & Support
<div align="center">
Created with ❤️ by Supriya Baghel

⭐ Star this repo if you find it helpful! ⭐
</div>

<div align="center">
Happy Coding! 🚀
Making code reviews faster, smarter, and more accessible for everyone.
</div>
