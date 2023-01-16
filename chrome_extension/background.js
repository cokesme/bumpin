chrome.action.onClicked.addListener((tab) => {
    console.log("injecting");
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ['content.js']
    });
  });