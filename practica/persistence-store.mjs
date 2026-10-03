/** Persistencia desacoplada de MA-Práctica. Código original GPL-3.0-or-later. */
import { emptyProgress, loadProgress, saveProgress } from './progress.mjs';

export class LocalProgressStore {
  constructor(storage) {
    this.storage = storage;
    this.kind = 'local';
  }

  load() {
    return loadProgress(this.storage);
  }

  save(progress) {
    return saveProgress(this.storage, progress);
  }

  clear() {
    return this.save(emptyProgress());
  }

  isAvailable() {
    return this.load().persistent;
  }
}

export function createLocalProgressStore(storage) {
  return new LocalProgressStore(storage);
}
