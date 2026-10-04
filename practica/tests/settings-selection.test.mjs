import test from 'node:test';
import assert from 'node:assert/strict';
import { createSettingsSelection } from '../settings-selection.mjs';

test('Elegir solo el área no cierra ni aplica: queda pendiente la modalidad', () => {
  const selection = createSettingsSelection();
  assert.deepEqual(selection.change('area'), { pending: true, ready: false });
  assert.equal(selection.pending, true);
  assert.equal(selection.ready, false);
});

test('Área y luego modalidad completan una única selección', () => {
  const selection = createSettingsSelection();
  selection.change('area');
  assert.deepEqual(selection.change('mode'), { pending: true, ready: true });
  selection.reset();
  assert.equal(selection.pending, false);
  assert.equal(selection.ready, false);
});

test('También funciona seleccionando modalidad antes del área', () => {
  const selection = createSettingsSelection();
  assert.equal(selection.change('mode').ready, false);
  assert.equal(selection.change('area').ready, true);
});

test('Repetir cambios en un mismo selector no equivale a cambiar ambas opciones', () => {
  const selection = createSettingsSelection();
  selection.change('area');
  assert.equal(selection.change('area').ready, false);
  assert.equal(selection.change('mode').ready, true);
});

test('Solo una opción puede aplicarse explícitamente y restablecer la selección', () => {
  const selection = createSettingsSelection();
  selection.change('mode');
  assert.equal(selection.pending, true);
  selection.reset();
  assert.deepEqual(selection.change('area'), { pending: true, ready: false });
  assert.throws(() => selection.change('unknown'), RangeError);
});
