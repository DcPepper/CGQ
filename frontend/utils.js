var db = {};

// We'll use a function to process each table row one at a time
function processRows(rows, index) {
  if (index >= rows.length) {
    console.log("All rows processed. Database:", db);
    return;
  }
  
  var tr = rows[index];
  var a = tr.querySelector('a');
  if (!a || !a.href) {
    // Skip this row if there's no link
    processRows(rows, index + 1);
    return;
  }
  
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // This is called when the request is complete
      var parser = new DOMParser();
      var text = this.responseText;
      var dom = parser.parseFromString(text, 'text/html');
      
      var kanjiElement = dom.querySelector('.kanji_character');
      if (kanjiElement) {
        var kanji = kanjiElement.innerText;
        db[kanji] = {};
        
        var translationElement = dom.querySelector('.translation');
        if (translationElement) {
          db[kanji]["translate"] = translationElement.innerText;
        }
        
        for (var def of dom.querySelectorAll('h2')) {
          if (def.innerText == "Onyomi") {
            var onyomiElement = def.nextElementSibling.querySelector('.onyomi');
            if (onyomiElement) {
              db[kanji]["onyomi"] = onyomiElement.innerText;
            }
          } else if (def.innerText == "Kunyomi") {
            var tdElements = def.nextElementSibling.querySelectorAll('td');
            if (tdElements.length > 1) {
                text = tdElements[1].innerText.split('\n');

              db[kanji]["kun_translate"] = text[0] == '' ? text[1]: text[0];
              db[kanji]["kun_kanji"] = tdElements[0].innerText;
            }
          }
        }
      }
      
      // Process the next row
      processRows(rows, index + 1);
    }
  };
  
  xmlhttp.open('GET', a.href, true); // true for asynchronous
  xmlhttp.send();
}

// Start processing from the first row
var rows = document.querySelectorAll('tr');
processRows(rows, 0);
