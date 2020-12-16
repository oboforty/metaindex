
export const Page = Enum(
  'index',
  'view',
);

export const PageContext = Enum(
  'metabolome',
  'structure',
  'pathway',
  'onthology'
);


export class Navigator {

  constructor() {
    this.page = Page.index;
    this.context = PageContext.metabolome;
  }

  navigate_to(page) {
    // todo: open appropriate vue.js page

    // todo: update url automatically with right page
  }
}