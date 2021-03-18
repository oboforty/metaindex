export const template = `<table class="table table-sm table-borderless table-hover">
  <tr>
    <th class="text-success">Formula</th>
    <td>
      <div v-for="formula in meta.formula">
        <span class="btn-block text-brand text-left" v-html="molcol(formula)"></span>
      </div>
    </td>
  </tr>
  <tr>
    <th class="text-success">InChI</th>
    <td>
      <!-- TODO: inchikey !-->
      
      <div v-for="inchi in meta.inchi">
        <span class="btn-block text-brand text-left" v-html="molcol(inchi)"></span>
      </div>

    </td>
  </tr>
  
  <tr>
    <th class="text-success">SMILES</th>
    <td>
      <div v-for="smiles in meta.smiles">
        <span class="btn-block text-brand text-left" v-html="molcol(smiles)"></span>
      </div>
    </td>
  </tr>
  <!-- <tr>
    <th class="text-success">Mass<sup class="text-info sup-smol">average</sup></th>
    <td>{{ meta.mass }}</td>
  </tr>
  <tr>
    <th class="text-success">Mass<sup class="text-info sup-smol">monoisotopic</sup></th>
    <td>{{ meta.monoisotopic_mass }}</td>
  </tr> -->
</table>`;