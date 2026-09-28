import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Natural Language Grid Assistant",
    page_icon="⚡",
    layout="wide"
)

# Load grid data
@st.cache_data
def load_data():
    df = pd.read_csv("grid_data.csv")
    return df


df = load_data()

# Title
st.title("⚡ Natural-Language Grid Assistant")

st.write(
    "Ask questions about power consumption, voltage, "
    "current, frequency, and grid status."
)

# Display grid data
st.subheader("📊 Grid Telemetry Data")

st.dataframe(
    df,
    use_container_width=True
)

# Query section
st.subheader("💬 Ask the Grid Assistant")

query = st.text_input(
    "Enter your question:",
    placeholder="Example: What is the highest power consumption?"
)


def process_query(query):

    q = query.lower().strip()

    # Average power
    if "average power" in q or "average consumption" in q:

        value = df["power_consumption"].mean()

        return (
            f"The average power consumption is "
            f"{value:.2f} units."
        )

    # Highest power
    elif (
        "highest power" in q
        or "maximum power" in q
        or "peak power" in q
        or "highest consumption" in q
    ):

        row = df.loc[
            df["power_consumption"].idxmax()
        ]

        return (
            f"The highest power consumption is "
            f"{row['power_consumption']} units "
            f"at {row['timestamp']}."
        )

    # Lowest power
    elif (
        "lowest power" in q
        or "minimum power" in q
        or "lowest consumption" in q
    ):

        row = df.loc[
            df["power_consumption"].idxmin()
        ]

        return (
            f"The lowest power consumption is "
            f"{row['power_consumption']} units "
            f"at {row['timestamp']}."
        )

    # Average voltage
    elif "average voltage" in q:

        value = df["voltage"].mean()

        return (
            f"The average voltage is "
            f"{value:.2f} V."
        )

    # Voltage
    elif "voltage" in q:

        row = df.iloc[-1]

        return (
            f"The latest recorded voltage is "
            f"{row['voltage']} V."
        )

    # Current
    elif "current" in q:

        row = df.iloc[-1]

        return (
            f"The latest recorded current is "
            f"{row['current']} A."
        )

    # Frequency
    elif "frequency" in q:

        value = df["frequency"].mean()

        return (
            f"The average grid frequency is "
            f"{value:.2f} Hz."
        )

    # Grid status
    elif "status" in q or "grid condition" in q:

        row = df.iloc[-1]

        return (
            f"The latest grid status is "
            f"{row['status']}."
        )

    # Latest power
    elif (
        "current power" in q
        or "latest power" in q
        or "latest consumption" in q
    ):

        row = df.iloc[-1]

        return (
            f"The latest recorded power consumption is "
            f"{row['power_consumption']} units "
            f"at {row['timestamp']}."
        )

    # Help
    elif "help" in q or "what can you do" in q:

        return """
I can answer questions about:

• Average power consumption
• Highest power consumption
• Lowest power consumption
• Voltage
• Current
• Frequency
• Grid status
• Latest power consumption
"""

    # Unknown query
    else:

        return (
            "I could not understand the question. "
            "Try asking about power consumption, voltage, "
            "current, frequency, or grid status."
        )


# Process user question
if query:

    answer = process_query(query)

    st.success(answer)
