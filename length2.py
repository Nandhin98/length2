  def reverseWord(Sentence): 
  	words = Sentence.split(" ") 
  	newWords = [word[::-1] for word in words] 
  	newSentence = " ".join(newWords) 
  	return newSentence 
  Sentence = input()
  print(reverseWord(Sentence))
