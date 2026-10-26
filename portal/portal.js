(() => {
  'use strict';
  const check = document.getElementById('prediccion-form');
  if (check) check.addEventListener('submit', event => {
    event.preventDefault();
    const value = new FormData(check).get('forma');
    const responses = {
      '3x3': 'Coincide: son tres ventas y tres columnas de datos. El índice etiqueta las filas aparte. Ahora explica por qué ocho unidades no significan ocho filas.',
      '3x4': 'Revisa el índice: etiqueta las filas y no añade una columna de datos. La forma es (3, 3). Compara los tres nombres de tabla.columns con tabla.index.',
      '8x3': 'Revisa la unidad por fila: aquí cada fila es una venta. Las ocho unidades son una suma, no el número de registros. La forma es (3, 3).'
    };
    document.getElementById('prediccion-respuesta').textContent = responses[value] || 'Selecciona una opción.';
  });
  const form = document.getElementById('bitacora-form');
  if (!form) return;
  const key = 'ds-track:piloto:02.01:bitacora:v1';
  const status = document.getElementById('estado-guardado');
  const names = ['participante', 'pareja', 'estado', 'prediccion', 'observado', 'explicacion', 'evidencia', 'siguiente'];
  const read = () => Object.fromEntries(names.map(n => [n, form.elements.namedItem(n).value]));
  const say = text => { status.textContent = text; };
  try {
    const saved = JSON.parse(localStorage.getItem(key) || 'null');
    if (saved && saved.version === 1 && saved.datos) {
      for (const name of names) if (typeof saved.datos[name] === 'string') form.elements.namedItem(name).value = saved.datos[name];
      say('Borrador recuperado de este navegador. Puedes editarlo y volver a guardar.');
    }
  } catch (_) { say('No se pudo recuperar el borrador. Puedes escribir y descargar tu nota.'); }
  form.addEventListener('input', () => say('Tienes cambios sin guardar. Puedes guardarlos o descargarlos.'));
  form.addEventListener('submit', event => {
    event.preventDefault();
    try {
      localStorage.setItem(key, JSON.stringify({version: 1, fecha: new Date().toISOString(), datos: read()}));
      say('Borrador guardado en este navegador. Descárgalo para conservarlo junto al notebook.');
    } catch (_) { say('Este navegador no permitió guardar. Descarga tu bitácora para conservarla.'); }
  });
  document.getElementById('exportar').addEventListener('click', () => {
    const d = read();
    const text = `# Bitácora personal — 02.01\n\nFecha de exportación: ${new Date().toISOString()}\nParticipante: ${d.participante}\nCompañero/a: ${d.pareja}\nEstado declarado: ${d.estado}\n\n## Predicción\n\n${d.prediccion}\n\n## Observación y comprobación\n\n${d.observado}\n\n## Mi explicación\n\n${d.explicacion}\n\n## Evidencia\n\n${d.evidencia}\n\n## Ayudas, dudas y siguiente paso\n\n${d.siguiente}\n\nRegistro personal: no acredita una revisión automática ni aprendizaje completado.\n`;
    const url = URL.createObjectURL(new Blob([text], {type: 'text/markdown;charset=utf-8'}));
    const a = document.createElement('a'); a.href = url; a.download = 'bitacora-02.01.md'; a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    say('Bitácora descargada con los valores actuales. El borrador guardado solo cambia al pulsar Guardar.');
  });
})();
