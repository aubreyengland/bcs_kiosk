import xapi from 'xapi';

// Inactivity Timeout (milliseconds)
const INACTIVITY_TIMEOUT = 45000; // 45 seconds

// Timer Variable
let inactivityTimer;

// Root Menu Mapping (Button IDs -> Panels)
const root_directory = {
    go_to_tech_admins: 'tech_admins',
    go_to_project_contacts: 'project_contacts',
    go_to_cdw_contacts: 'cdw_contacts',
};

// Mapping widget IDs to contacts
const tech_admins = {  
  dial_Dara_Foy: 'dara.foy@bcsdk12.net',
  dial_Sarah_Mayberry: 'sarah.mayberry@bcsdk12.net',
  dial_Joshua_Moneypenny: 'joshua.moneypenny@bcsdk12.net',
};

const project_contacts = {
  dial_Carlos_Madera: 'carlos.madera@bcsdk12.net',
  dial_Joseph_Taylor: 'joseph.taylor@bcsdk12.net',
};

const cdw_contacts = {  
  dial_Aubrey_England: 'aubreng@cdw.com',
  dial_Mike_Robinson: 'mike.robinson@cdw.com',
  dial_Breannan_Geis: 'bregeis@cdw.com',
};

// Combine all contacts for easier lookup
const contacts = { ...tech_admins, ...project_contacts, ...cdw_contacts };

// Panel IDs (defined in Webex UI Extensions)
const panels = {
    root_directory: 'root_directory', // Must exist in UI Extensions
    tech_admins: 'tech_admins',
    project_contacts: 'project_contacts',
    cdw_contacts: 'cdw_contacts',
};

// Function to reset inactivity timer
function resetInactivityTimer() {
    clearTimeout(inactivityTimer);
    inactivityTimer = setTimeout(() => {
        console.log('Inactivity timeout reached. Returning to main menu.');
        openPanel('root_directory');
    }, INACTIVITY_TIMEOUT);
}

// Function to dial a contact
function dial(number) {
  if (!number) {
    console.error('Invalid number');
    return;
  }
  console.log(`Dialing: ${number}`);
  xapi.Command.Dial({ Number: number }).catch((error) => {
    console.error(`Dial command failed: ${error}`);
  });
  resetInactivityTimer();
}

// Function to switch UI panels
function openPanel(panelId) {
  console.log(`Opening Panel: ${panelId}`);
  xapi.Command.UserInterface.Extensions.Panel.Open({ PanelId: panelId }).catch((error) => {
    console.error(`Failed to open panel: ${error}`);
  });
  resetInactivityTimer();
}

// Listen for button presses
function listenToGui() {
  xapi.Event.UserInterface.Extensions.Widget.Action.on((event) => {
    if (event.Type === 'clicked') {
      console.log(`Button pressed: ${event.WidgetId}`);

      // Handle dialing contacts
      if (Object.hasOwnProperty.call(contacts, event.WidgetId)) {
        dial(contacts[event.WidgetId]);
      } 
      // Handle switching panels
      else if (Object.hasOwnProperty.call(panels, event.WidgetId)) {
        openPanel(panels[event.WidgetId]);
      }
      // Handle navigation from root directory
      else if (Object.hasOwnProperty.call(root_directory, event.WidgetId)) {
        openPanel(root_directory[event.WidgetId]);
      }
      else {
        console.warn(`Unknown widget ID: ${event.WidgetId}`);
      }
    }
  });
}

// Start listening for button presses
listenToGui();
resetInactivityTimer(); // Start inactivity timer at macro load