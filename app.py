# -----------------------------
        
        # -----------------------------

        st.header("🤖 Ask Your Data")

        question = st.text_input(
            "💬 Ask a question about your dataset",
            placeholder="Example: What is the average age?"
        )

        if st.button("🔍 Analyze"):

            if question.strip() == "":
                st.warning("Please enter a question.")

            else:

                q = question.lower()

                found_column = None

                # Find the column mentioned in the question
                for column in numerical_columns:

                    column_words = column.lower().replace("_", " ")

                    if column_words in q:
                        found_column = column
                        break

                # If exact column name was not found,
                # try matching individual words
                if found_column is None:

                    for column in numerical_columns:

                        words = column.lower().replace("_", " ").split()

                        for word in words:

                            if len(word) > 2 and word in q:
                                found_column = column
                                break

                        if found_column is not None:
                            break

                if found_column is not None:

                    data = df[found_column].dropna()

                    # Mean
                    if (
                        "average" in q
                        or "mean" in q
                    ):

                        answer = data.mean()

                        st.success(
                            f"📊 The average of "
                            f"**{found_column}** is "
                            f"**{answer:.2f}**."
                        )

                    # Median
                    elif "median" in q:

                        answer = data.median()

                        st.success(
                            f"📊 The median of "
                            f"**{found_column}** is "
                            f"**{answer:.2f}**."
                        )

                    # Maximum
                    elif (
                        "maximum" in q
                        or "highest" in q
                        or "maximum value" in q
                        or "max" in q
                    ):

                        answer = data.max()

                        st.success(
                            f"⬆️ The highest value of "
                            f"**{found_column}** is "
                            f"**{answer:.2f}**."
                        )

                    # Minimum
                    elif (
                        "minimum" in q
                        or "lowest" in q
                        or "minimum value" in q
                        or "min" in q
                    ):

                        answer = data.min()

                        st.success(
                            f"⬇️ The lowest value of "
                            f"**{found_column}** is "
                            f"**{answer:.2f}**."
                        )

                    # Total
                    elif (
                        "total" in q
                        or "sum" in q
                    ):

                        answer = data.sum()

                        st.success(
                            f"➕ The total of "
                            f"**{found_column}** is "
                            f"**{answer:.2f}**."
                        )

                    # Count
                    elif (
                        "how many" in q
                        or "count" in q
                        or "number of" in q
                    ):

                        answer = data.count()

                        st.success(
                            f"🔢 There are **{answer}** "
                            f"valid values in "
                            f"**{found_column}**."
                        )

                    else:

                        st.info(
                            "Try asking about "
                            "**average, median, highest, "
                            "lowest, total, or count**."
                        )
