library(tm)
data(crude)

crude
# reading and displaying all the
# 14 articles from crude
inspect(crude[[14]])
# removing the punctuation like,. and _
inspect(
    removePunctuation(crude[[14]],
        preserve_intra_word_contraction = FALSE,
        preserve_intra_word_dashes = FALSE
    )
)
inspect(removeNumbers(crude[[14]]))
# to check the stop words

# removing the stop words
inspect(removeWords(crude[[14]], stopwords("english")))