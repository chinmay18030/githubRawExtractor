import githubRawxtractor

ex = githubRawExtractor.Extractor("https://raw.githubusercontent.com/chinmay18030/handTracker/main/TrackHandModule.py")
text = ex.extract()
print(text)
ex.execute()
