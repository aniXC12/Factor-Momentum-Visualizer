# 🤝 Contributing to Factor Momentum Visualizer

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

---

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Development Setup](#development-setup)
4. [Coding Standards](#coding-standards)
5. [Submitting Changes](#submitting-changes)
6. [Reporting Bugs](#reporting-bugs)
7. [Suggesting Features](#suggesting-features)

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. We pledge to:

- Be respectful of differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

---

## 🚀 How to Contribute

There are many ways to contribute:

### 1. **Report Bugs** 🐛
Found a bug? Please open an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, etc.)

### 2. **Suggest Features** 💡
Have an idea? Open an issue with:
- Clear description of the feature
- Use case / motivation
- Proposed implementation (if any)
- Alternative solutions considered

### 3. **Improve Documentation** 📚
- Fix typos
- Add examples
- Clarify explanations
- Add tutorials

### 4. **Submit Code** 💻
- Fix bugs
- Implement features
- Add tests
- Optimize performance

---

## 🛠️ Development Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment (recommended)

### Setup Steps

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/factor-momentum-visualizer.git
   cd factor-momentum-visualizer
   ```

3. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

5. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

6. **Make your changes**
   - Write code
   - Add tests
   - Update documentation

7. **Test your changes**
   ```bash
   streamlit run app.py
   # Test thoroughly!
   ```

---

## 📝 Coding Standards

### Python Style Guide

Follow **PEP 8** guidelines:

```python
# Good
def calculate_sharpe_ratio(returns, risk_free_rate=0):
    """
    Calculate Sharpe ratio
    
    Args:
        returns: Series of returns
        risk_free_rate: Risk-free rate (default 0)
    
    Returns:
        Sharpe ratio as float
    """
    excess_returns = returns - risk_free_rate
    return excess_returns.mean() / excess_returns.std()

# Bad
def calc_sharpe(r,rf=0):
    return (r-rf).mean()/(r-rf).std()
```

### Code Organization

- **Modular**: Break code into logical modules
- **Documented**: Add docstrings to all functions
- **Typed**: Use type hints where appropriate
- **Tested**: Write tests for new functionality

### File Structure

```
factor_momentum_visualizer/
├── app.py                    # Main app (keep clean!)
├── data/                     # Data modules
├── factors/                  # Factor calculations
├── backtest/                 # Backtesting logic
├── plots/                    # Visualization functions
└── utils/                    # Helper functions
```

### Commit Messages

Use conventional commits format:

```
type(scope): subject

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

Examples:
```bash
git commit -m "feat(factors): add Fama-French 5-factor model"
git commit -m "fix(backtest): correct drawdown calculation"
git commit -m "docs(readme): add deployment instructions"
```

---

## 📤 Submitting Changes

### Pull Request Process

1. **Update documentation**
   - Update README.md if needed
   - Add docstrings to new functions
   - Update CHANGELOG.md

2. **Test thoroughly**
   - Run the app locally
   - Test edge cases
   - Ensure no errors

3. **Create Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Performance improvement

## Testing
How you tested the changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tested locally
- [ ] No breaking changes
```

### Review Process

- Maintainers will review your PR
- Address any feedback
- Once approved, your PR will be merged!

---

## 🐛 Reporting Bugs

### Before Submitting

- Check existing issues
- Verify it's actually a bug
- Collect relevant information

### Bug Report Template

```markdown
**Description**
Clear description of the bug

**To Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What should happen

**Screenshots**
If applicable

**Environment**
- OS: [e.g., macOS 13.0]
- Python: [e.g., 3.9.7]
- Browser: [e.g., Chrome 120]

**Additional Context**
Any other relevant information
```

---

## 💡 Suggesting Features

### Feature Request Template

```markdown
**Is your feature related to a problem?**
Describe the problem

**Describe the solution**
What you'd like to happen

**Describe alternatives**
Other solutions you've considered

**Additional context**
Mockups, examples, etc.
```

---

## 🎯 Priority Areas

We're especially interested in:

### High Priority
- [ ] Performance optimizations
- [ ] Additional factor models
- [ ] Enhanced visualizations
- [ ] Better error handling

### Medium Priority
- [ ] Multi-factor composites
- [ ] Regime detection
- [ ] Transaction cost modeling
- [ ] Risk parity allocation

### Low Priority
- [ ] UI/UX improvements
- [ ] Additional export formats
- [ ] Internationalization
- [ ] Mobile responsiveness

---

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Given credit in documentation

---

## 📚 Resources

### Learn More
- [Streamlit Documentation](https://docs.streamlit.io)
- [Python Style Guide (PEP 8)](https://pep8.org)
- [Git Best Practices](https://git-scm.com/book/en/v2)

### Community
- GitHub Discussions
- Issues section
- Pull Requests

---

## ❓ Questions?

If you have questions:
1. Check existing documentation
2. Search issues
3. Ask in GitHub Discussions
4. Open a new issue

---

## 🙏 Thank You!

Every contribution helps make this project better. Whether you're:
- Fixing a typo
- Adding a feature
- Reporting a bug
- Improving docs

**Your contribution matters!** 🎉

Happy coding! 🚀
