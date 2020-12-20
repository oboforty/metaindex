export const template = `<table class="table table-sm table-borderless table-hover">
  <tr>
    <th class="text-success">Formula</th>
    <td v-html="molcol( meta.formula )">
    </td>
  </tr>
  <tr>
    <th class="text-success">InChI</th>
    <td>
      <span v-html="molcol( meta.inchi )"></span>
      <br/>
      <span class="small">{{ meta.inchikey }}</span>
    </td>
  </tr>
  
  <tr>
    <th class="text-success">SMILES</th>
    <td>
      <span v-html="molcol( meta.smiles )"></span>
    </td>
  </tr>
  <tr>
    <th class="text-success">Mass<sup class="text-info sup-smol">average</sup></th>
    <td>{{ meta.mass }}</td>
  </tr>
  <tr>
    <th class="text-success">Mass<sup class="text-info sup-smol">monoisotopic</sup></th>
    <td>{{ meta.monoisotopic_mass }}</td>
  </tr>
</table>`;