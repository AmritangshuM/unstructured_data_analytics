
driver = webdriver.Chrome('C:/Users/bandi/Desktop/Text Analytics/TA Session/chromedriver_win32/chromedriver')
driver.get('https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p702')

comments = pd.DataFrame(columns = ['Date','user_id','comments']) 
ids = driver.find_elements_by_xpath("//*[contains(@id,'Comment_')]")
comment_ids = []
for i in ids:
    comment_ids.append(i.get_attribute('id'))

for x in comment_ids:
    #Extract dates from for each user on a page
    user_date = driver.find_elements_by_xpath('//*[@id="' + x +'"]/div/div[2]/div[2]/span[1]/a/time')[0]
    date = user_date.get_attribute('title')

    #Extract user ids from each user on a page
    userid_element = driver.find_elements_by_xpath('//*[@id="' + x +'"]/div/div[2]/div[1]/span[1]/a[2]')[0]
    userid = userid_element.text

    #Extract Message for each user on a page
    user_message = driver.find_elements_by_xpath('//*[@id="' + x +'"]/div/div[3]/div/div[1]')[0]
    comment = user_message.text
                                   
    #Adding date, userid and comment for each user in a dataframe    
    comments.loc[len(comments)] = [date,userid,comment]
