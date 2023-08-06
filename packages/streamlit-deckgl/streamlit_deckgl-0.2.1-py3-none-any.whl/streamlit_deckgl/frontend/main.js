const { DeckGL, JSONConverter, carto } = deck;

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */

function onRender(event) {
  // Only run the render code the first time the component is loaded.
  if (!window.rendered) {
    const {
      spec,
      tooltip,
      height,
      customLibraries,
      configuration,
      decription,
      events,
      description,
    } = event.detail.args;

    const eventlist = events && events.map((event) => `deck-${event}-event`);

    const container = document.getElementById("root");
    container.style.width = window.innerWidth - 10 + "px";
    container.style.height = height - 10 + "px";

    const mapEventHandler = (eventType, info) => {
      if (events && eventlist.includes(eventType) && info.object) {
        Streamlit.setComponentValue(info.object);
      }
    };

    const deckInstance = createDeck({
      container,
      jsonInput: JSON.parse(spec),
      tooltip,
      customLibraries,
      configuration,
      handleEvent: mapEventHandler,
    });

    if (description) {
      for (const key in description) {
        if (
          ["top-right", "top-left", "bottom-right", "bottom-left"].includes(key)
        ) {
          const pos = key.split("-");
          const style = `position: absolute; ${pos[0]}:10px; ${pos[1]}:10px;`;
          const div = document.createElement("div");
          div.innerHTML = description[key];
          div.style = style;
          container.appendChild(div);
        }
      }
    }

    Streamlit.setFrameHeight(height);
    window.rendered = true;
  }
}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady();
// Render with the correct height, if this is a fixed-height component
