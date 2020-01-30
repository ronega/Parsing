def CurrentPageSoup(WebDriver):
    from bs4 import BeautifulSoup
    html_new = WebDriver.page_source
    soup = BeautifulSoup(html_new, features="html.parser")
    search = soup.find_all(class_='htDimmed')
    data_for_df = []
    for data in search:
        if data.find('fgis-h-table-limited-text-cell') == None:
            data_for_df.append("Нет информации")
        else:
            result = str(data.find('fgis-h-table-limited-text-cell').get_text())
            data_for_df.append(result)
    data_for_df = data_for_df[11:-11]
    return data_for_df

