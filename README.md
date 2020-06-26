# Sentiment-Analysis-Classification-of-Restaurant-Reviews-into-Positive-or-Negative-reviews-
Classification of Restaurant Reviews into Positive or Negative reviews.                                                                                                             
Dataset : This Dataset contain 1000 reviews given by customer to the Restaurant.It is in the form of .tsv(tab seprated values) format.
Libraries used : numpy,pandas,sklearn,keras,nltk,re                                                                                                    
Steps:                                                                                                                                                                         1)Importing Libraries and Dataset                                                               
2)Clearing text                                                                                                                                       
    a)replacing punctuation with spaces b)making lower case c)splitting sentences into words d)stemming e)Removing Stopwords f)Joining                                                                                       
3)Creating Bag of words                                                                                                                     
4)splitting Dataset into training and Testing set                                                                                            
5)Modeling                                                                                                                                   
Used 2 classification models:                                                                                                         
SVM with kernel sigmoid.                                                                                                                        
Training accuracy = 80.38% with standard deviation among training 3.99%                                                                         
Testing accuracy = 80.50%                                                                                                                           
Logistic Regression.                                                                                                                                   
Training accuracy = 80.75% with standard deviation among training 3.12%                                                                       
Testing accuracy = 80.50%                                                                                                                           
6)Also classified single review using both classifier at the end.                                                                                                      
Note: Models with accuracy above 80% are good models we can use them for real life applications.
