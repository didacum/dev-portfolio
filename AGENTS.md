# 1. Project Context
- **Domain:** Software Development Portfolio.
- **Tech Stack:** Python, Reflex Framework.
- **Goal:** Display projects, leveraging Reflex's pure Python UI/backend paradigm without falling back to traditional web technologies.

# 2. Architecture & Constraints
- **Directory Structure Rule:** The project MUST adhere strictly to the following directory separation. Commits violating this structure MUST be rejected:
  - `components/`: Pure, reusable Reflex UI components.
  - `views/`: Main page compositions and layout wrappers.
  - `styles/`: Reflex-based styling dictionaries and theme configurations.
  - `assets/`: Static files (images, fonts).
- **Strict UI Constraint (No Web Primitives):** - ⛔ PROHIBITED: The use of raw HTML tags, inline standard CSS, or `.html`/`.css` files.
  - ✅ REQUIRED: All UI elements and styling MUST be implemented exclusively via Reflex components (`rx.*`) and Reflex style dictionaries.
- **Component Design:** Components in `components/` must be modular and decoupled from the main page logic.

# 3. Data Flow & Security
- **Data Source:** Project data is strictly static and redirection-based. The application MUST use GitHub repository URLs to redirect users, avoiding complex API state management for the repositories.
- **Secret Management (Zero-Trust):** - ⛔ PROHIBITED: Hardcoding of credentials, API keys, personal access tokens, or any sensitive configuration inside the source code.
  - ✅ REQUIRED: All environment-dependent or sensitive data MUST be injected via Environment Variables (`.env` file in local, environment variables in production). Code diffs must only show references to `os.getenv()` or Reflex's config equivalent.

# 4. Git & Commits
- **Commit Convention:** Commits MUST strictly follow the `Conventional Commits` specification (e.g., `feat:`, `fix:`, `refactor:`, `chore:`).
- **Branching Model (Gitflow):** - ⛔ PROHIBITED: Direct commits to `main`, `master`, or `develop` branches.
  - ✅ REQUIRED: All new features or fixes MUST be developed in isolated branches (e.g., `feature/*`, `bugfix/*`).
- **Integration Rule:** Code MUST reach the remote repository strictly through Pull Requests (PRs).