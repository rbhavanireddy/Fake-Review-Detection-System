def check_fake_review(review, rating):
    score = 0

    positive_words = ["amazing", "excellent", "superb", "best", "perfect"]
    count = 0

    for word in positive_words:
        if word in review.lower():
            count += 1

    if count >= 3:
        score += 30

    if len(review.split()) < 3:
        score += 20

    words = review.lower().split()
    if len(words) != len(set(words)):
        score += 20

    if rating == 5:
        score += 10

    return score


def trust_score(total_reviews):
    if total_reviews > 20:
        return "High Trust"
    elif total_reviews > 10:
        return "Medium Trust"
    else:
        return "Low Trust"


review = input("Enter review: ")
rating = int(input("Enter rating (1-5): "))
total_reviews = int(input("Total reviews by user: "))

fake_score = check_fake_review(review, rating)

if fake_score >= 50:
    print("⚠ Fake Review Detected")
else:
    print("✅ Genuine Review")

print("Fake Score:", fake_score)

print("Reviewer Trust Level:", trust_score(total_reviews))
