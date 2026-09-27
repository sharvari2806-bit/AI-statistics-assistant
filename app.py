import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI Statistics Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Powered Statistics Assistant")
st.write("Upload any CSV dataset and explore it using statistics.")

uploaded_file = st.file_uploader(
    "📁 Upload your CSV dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully! ✅")

    # Dataset Preview
    st.header("📋 Dataset Preview")
    st.dataframe(df, use_container_width=True)

    # Dataset Information
    st.header("📊 Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    numerical_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numerical_columns) > 0:

        # Statistical Summary
        st.header("🔢 Statistical Summary")

        st.dataframe(
            df[numerical_columns].describe(),
            use_container_width=True
        )

        # Data Visualization
        st.header("📈 Data Visualization")

        selected_column = st.selectbox(
            "Choose a numerical column",
            numerical_columns
        )

        fig, ax = plt.subplots()

        ax.hist(
            df[selected_column].dropna(),
            bins=10
        )

        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")
        ax.set_title(
            f"Distribution of {selected_column}"
        )

        st.pyplot(fig)

        # Correlation Analysis
        if len(numerical_columns) >= 2:

            st.header("🔗 Correlation Analysis")

            x_column = st.selectbox(
                "Select first variable",
                numerical_columns,
                key="x_column"
            )

            y_column = st.selectbox(
                "Select second variable",
                numerical_columns,
                key="y_column"
            )

            correlation = df[x_column].corr(
                df[y_column]
            )

            st.metric(
                "Correlation",
                f"{correlation:.2f}"
            )

            fig, ax = plt.subplots()

            ax.scatter(
                df[x_column],
                df[y_column]
            )

            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_title(
                f"{x_column} vs {y_column}"
            )

            st.pyplot(fig)

        # Outlier Detection
        st.header("🚨 Outlier Detection")

        outlier_column = st.selectbox(
            "Choose a column to check for outliers",
            numerical_columns,
            key="outlier_column"
        )

        data = df[outlier_column].dropna()

        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)
        iqr = q3 - q1

        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr

        outliers = df[
            (df[outlier_column] < lower_limit)
            | (df[outlier_column] > upper_limit)
        ]

        st.write(f"Q1: **{q1:.2f}**")
        st.write(f"Q3: **{q3:.2f}**")
        st.write(f"IQR: **{iqr:.2f}**")
        st.write(
            f"Lower limit: **{lower_limit:.2f}**"
        )
        st.write(
            f"Upper limit: **{upper_limit:.2f}**"
        )

        if len(outliers) > 0:

            st.warning(
                f"🚨 {len(outliers)} possible "
                f"outlier(s) detected."
            )

            st.dataframe(
                outliers,
                use_container_width=True
            )

        else:

            st.success(
                "✅ No possible outliers detected."
            )

        # Ask Your Data
        st.header("🤖 Ask Your Data")

        question = st.text_input(
            "💬 Ask a question about your dataset",
            placeholder="Example: What is the average age?"
        )
