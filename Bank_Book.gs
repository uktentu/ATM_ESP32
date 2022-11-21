var sheetId = "1gCtdFlkRZ3fKysncwiW9RNEA0WbbmLeWPS-1_DkpV94";
var ss = SpreadsheetApp.openById(sheetId);
var user_sheet = "User";
var sheet = ss.getSheetByName(user_sheet);

function doGet(e) {
  var username = e.parameter.username;
  var password = e.parameter.password;
  var login = e.parameter.login;
  var acc_no = e.parameter.acc_no;
  var balance = e.parameter.balance;
  var credit = e.parameter.credit;
  var debit = e.parameter.debit;
  var create = e.parameter.create;
  var name = e.parameter.name;
  var mini_sheet = e.parameter.mini_sheet;

  if (login !== undefined) {
    var status = user_login(username, password);
    return ContentService.createTextOutput(status);
  }

  if (balance !== undefined) {
    var acc_book = ss.getSheetByName(String(acc_no));
    balance = String(acc_book.getRange(acc_book.getLastRow(), 4).getValues());
    return ContentService.createTextOutput(balance);
  }

  if (credit !== undefined) {
    var acc_book = ss.getSheetByName(String(acc_no));
    acc_book.appendRow([acc_book.getLastRow(), , credit, Number(acc_book.getRange(acc_book.getLastRow(), 4).getValues()) + Number(credit)])
    return ContentService.createTextOutput("y");
  }

  if (debit !== undefined) {
    var acc_book = ss.getSheetByName(String(acc_no));
    if (Number(acc_book.getRange(acc_book.getLastRow(), 4).getValues()) - debit > 0) {
      acc_book.appendRow([acc_book.getLastRow(), debit, , Number(acc_book.getRange(acc_book.getLastRow(), 4).getValues()) - Number(debit)])
      return ContentService.createTextOutput("y");
    }
    else {
      return ContentService.createTextOutput("n");
    }
  }

  if (mini_sheet !== undefined) {
    var acc_book = ss.getSheetByName(String(acc_no));
    var last = acc_book.getLastRow();
    var text = "";
    var mini = acc_book.getRange('B1:D1').getValues();
    for (var k = 0; k < 3; k += 1) {
      text += String(mini[0][k]);
      if (k != 2) {
        text += "----";
      }
    }
    text += "\n";
    if (last < 6) {
      var mini = acc_book.getRange('B2:D5').getValues();
    }
    else {
      var mini = acc_book.getRange("B" + String(last - 5) + ":D" + String(last)).getValues();
    }
    for (var j = 0; j < mini.length; j += 1) {
      for (var i = 0; i < mini[j].length; i += 1) {
        if (String(Number(mini[j][i])) == mini[j][i]) {
          text += String(mini[j][i]);
          if(i!=mini[j].length-1){
            text+="----";
          }
        }
        else {
          text += String("----------");
        }
      }
      text += String("\n");
    }
    return ContentService.createTextOutput(text);
  }





  if (create !== undefined) {
    var status = user_create(username, password, name);
    return ContentService.createTextOutput(status);
  }

}
function user_login(username, password) {
  for (var c = 2; c <= sheet.getLastRow(); c = c + 1) {
    if (String(sheet.getRange(c, 1).getValues()) == username) {
      if (String(sheet.getRange(c, 2).getValues()) == password) {
        return (String(sheet.getRange(c, 3).getValues()) + ",acc=" + String(c - 1));
      }
    }
  }
  return "n";
}

function user_create(username, password, name) {
  for (var c = 2; c <= sheet.getLastRow(); c = c + 1) {
    if (String(sheet.getRange(c, 1).getValues()) == username) {
      return "n";
    }
  }
  var acc_no = sheet.getLastRow();
  sheet.appendRow([username, password, name, acc_no])
  var new_sheet = ss.insertSheet();
  new_sheet.setName(acc_no);
  new_sheet.appendRow(["S no", "Debit", "Credit", "Balance"]);
  new_sheet.appendRow(["1",,"15000","15000"]);
  return "y";
}
