/* Leaflet map setup for WildPath. */
const map = L.map('map', {
  scrollWheelZoom: true
}).setView(mapCenter, mapZoom);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

const markerIcon = L.divIcon({
  className: 'bird-marker',
  html: '<span>🐤</span>',
  iconSize: [24, 24],
  iconAnchor: [12, 12]
});

const bounds = [];

for (let i = 0; i < mapPoints.length; i++) {
  const point = mapPoints[i];
  const latLng = [point.latitude, point.longitude];
  bounds.push(latLng);

  let imageHtml = '';
  if (point.photo_url) {
    imageHtml = `<img src="${point.photo_url}" alt="Photo of ${point.common_name}" class="popup-photo">`;
  }

  const popupHtml = `
    <div class="popup-card">
      ${imageHtml}
      <strong>${point.common_name}</strong>
      <em>${point.scientific_name}</em>
      <p>${point.observed_on}</p>
      <p>${point.place_guess}</p>
      <a href="${point.uri}" target="_blank" rel="noreferrer">View observation</a>
    </div>
  `;

  L.marker(latLng, { icon: markerIcon }).addTo(map).bindPopup(popupHtml);
}

window.addEventListener('load', function () {
  map.invalidateSize();

  if (bounds.length > 0) {
    map.fitBounds(bounds, { padding: [32, 32], maxZoom: 12 });
  } else {
    map.setView(mapCenter, mapZoom);
  }
});