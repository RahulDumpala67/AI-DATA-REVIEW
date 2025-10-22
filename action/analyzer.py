import re

def analyze_data_script(filename):
    """
    Scans Python data-analysis scripts for common mistakes.
    """

    try:
        with open(filename, "r") as f:
            code = f.read()
    except FileNotFoundError:
        return "⚠️ No data file found for analysis."

    suggestions = []

    # 1️⃣ Check for missing NA handling
    if "dropna" not in code and "fillna" not in code:
        suggestions.append("⚠️ Missing data handling detected. Use dropna() or fillna().")

    # 2️⃣ Check for missing visualization
    if "plt.show" not in code and "sns." not in code:
        suggestions.append("📊 No visualization found. Consider adding charts for insights.")

    # 3️⃣ Check for inefficient loops
    if re.search(r"for .* in .*:", code) and "apply" not in code:
        suggestions.append("💡 Loops detected — try pandas vectorization or .apply() for performance.")

    # 4️⃣ Check for unimported libraries
    if "import pandas" not in code and "import numpy" not in code:
        suggestions.append("🧠 Missing data library imports (pandas/numpy).")

    if not suggestions:
        return "✅ Great job! No major data-analysis issues found."

    return "\n".join(suggestions)
