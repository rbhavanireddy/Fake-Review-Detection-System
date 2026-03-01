import streamlit as st

THRESHOLD = 50

# ------------------ Fake Review Detection Logic ------------------

def check_fake_review(review, rating, total_reviews):
    score = 0
    words = review.lower().split()

    positive_words = ["amazing", "excellent", "superb", "best", "perfect", "awesome"]
    negative_words = ["worst", "useless", "horrible", "waste", "bad"]

    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)

    # Excessive positive words
    if pos_count >= 3:
        score += 30

    # Excessive negative words
    if neg_count >= 3:
        score += 30

    # ALL CAPS review
    if review.isupper():
        score += 25

    # Too many exclamation marks
    if review.count("!") >= 3:
        score += 20

    # Very short review
    if len(words) < 3:
        score += 25

    # Rating mismatch logic
    if rating == 5 and pos_count >= 2:
        score += 15

    if rating == 1 and neg_count >= 2:
        score += 15

    # Low activity user
    if total_reviews < 5:
        score += 20

    return score


# ------------------ Trust Level Logic ------------------

def trust_score(total_reviews):
    if total_reviews > 20:
        return "High Trust"
    elif total_reviews > 10:
        return "Medium Trust"
    else:
        return "Low Trust"


# ------------------ Streamlit UI ------------------

st.title("Fake Review Detection System")

review = st.text_area("Enter Review")
rating = st.number_input("Enter Rating (1-5)", min_value=1, max_value=5)
total_reviews = st.number_input("Total Reviews by User", min_value=0)

if st.button("Check Review"):

    fake_score = check_fake_review(review, rating, total_reviews)
    trust = trust_score(total_reviews)

    if fake_score >= THRESHOLD:
        st.error("Fake Review Detected ❌")
    else:
        st.success("Genuine Review ✅")

    st.write("Fake Score:", fake_score)
    st.write("Reviewer Trust Level:", trust)
