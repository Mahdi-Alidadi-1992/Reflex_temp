/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext, useRef } from "react"
import { Event, refs } from "$/utils/state"
import { Box as RadixThemesBox, Button as RadixThemesButton, Flex as RadixThemesFlex, Text as RadixThemesText, Theme as RadixThemesTheme } from "@radix-ui/themes"
import { EventLoopContext, StateContexts } from "$/utils/context"
import { Drawer as VaulDrawer } from "vaul"
import { Menu as LucideMenu } from "lucide-react"
import theme from "$/utils/theme.js"
import NextHead from "next/head"
import { jsx } from "@emotion/react"



export function Img_20af87e7a058b3ff0067e50f73125a2d () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_b74dca6bc709ab653d06460c1e4544d4 = useCallback(((...args) => (addEvents([(Event("_call_script", ({ ["javascript_code"] : "document.getElementById('my_vstack')?.scrollTo({ top: 0, behavior: 'smooth' });" }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx("img",{css:({ ["objectFit"] : "contain", ["width"] : "200px", ["marginTop"] : "-20px", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) }),onClick:on_click_b74dca6bc709ab653d06460c1e4544d4,src:"/Yummak_Brand.png"},)

  )
}

export function Drawer__content_68acc0f80ef5a79c1e1e2911a94b0b2c () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_pointer_down_outside_e789981e22acca9929d0ff67080ef312 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.tesst_1___tesst_1____drawer_state.toggle_drawer", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
VaulDrawer.Content,
{css:({ ["left"] : "auto", ["right"] : "0", ["bottom"] : "0", ["top"] : "auto", ["position"] : "fixed", ["z_index"] : 50, ["display"] : "flex", ["height"] : "100%", ["width"] : "20em", ["padding"] : "2em", ["backgroundColor"] : "#FFF" }),onPointerDownOutside:on_pointer_down_outside_e789981e22acca9929d0ff67080ef312},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"column",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) })},
"Order"
,),jsx(
RadixThemesText,
{as:"p",css:({ ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) })},
"How It Works"
,),jsx(
RadixThemesText,
{as:"p",css:({ ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) })},
"On the Menu"
,),jsx(
RadixThemesButton,
{css:({ ["backgroundColor"] : "rgb(161, 169, 130)", ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) })},
"Sign Up / Log In"
,),jsx("img",{css:({ ["width"] : "60px", ["marginTop"] : "-10px", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) }),src:"/Shopping Cart.png"},)
,),)
  )
}

export function Img_5d46ab6f7f0fd2f78ff55b03fe6002e7 () {
  
  const reflex___state____state__tesst_1___tesst_1____header__state = useContext(StateContexts.reflex___state____state__tesst_1___tesst_1____header__state)





  
  return (
    jsx("img",{css:({ ["height"] : reflex___state____state__tesst_1___tesst_1____header__state.hero_size, ["width"] : "auto", ["zIndex"] : "1", ["position"] : "absolute" }),loading:"lazy",src:"/Page_icon.png"},)

  )
}

export function Drawer__root_5dc6a97cbb623ed010e78227f740428e () {
  
  const reflex___state____state__tesst_1___tesst_1____drawer_state = useContext(StateContexts.reflex___state____state__tesst_1___tesst_1____drawer_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    jsx(
VaulDrawer.Root,
{css:({ ["close"] : !(reflex___state____state__tesst_1___tesst_1____drawer_state.is_open) }),direction:"right",dismissible:true,modal:false,open:reflex___state____state__tesst_1___tesst_1____drawer_state.is_open},
jsx(
VaulDrawer.Trigger,
{asChild:true},
jsx(
RadixThemesFlex,
{},
jsx(LucideMenu,{css:({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "flex" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "flex" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 80em)"] : ({ ["display"] : "none" }), ["marginTop"] : "15px" }),onClick:((...args) => (addEvents([(Event("reflex___state____state.tesst_1___tesst_1____drawer_state.toggle_drawer", ({  }), ({  })))], args, ({  })))),size:40},)
,),),jsx(Drawer__overlay_c5bbf52c8c74d2bea05dcbf5e160b505,{},)
,jsx(
VaulDrawer.Portal,
{},
jsx(
Fragment,
{},
jsx(
RadixThemesTheme,
{css:{...theme.styles.global[':root'], ...theme.styles.global.body}},
jsx(Drawer__content_68acc0f80ef5a79c1e1e2911a94b0b2c,{},)
,),),),)
  )
}

export function Drawer__overlay_c5bbf52c8c74d2bea05dcbf5e160b505 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_e789981e22acca9929d0ff67080ef312 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.tesst_1___tesst_1____drawer_state.toggle_drawer", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(VaulDrawer.Overlay,{css:({ ["position"] : "fixed", ["left"] : "0", ["right"] : "0", ["bottom"] : "0", ["top"] : "0", ["z_index"] : 50, ["background"] : "rgba(0, 0, 0, 0.5)" }),onClick:on_click_e789981e22acca9929d0ff67080ef312},)

  )
}

export function Flex_25009d6dee37281ac7f1b43db42bc00a () {
  
  const ref_my_vstack = useRef(null); refs["ref_my_vstack"] = ref_my_vstack;
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const ref_target = useRef(null); refs["ref_target"] = ref_target;


  const on_scroll_dd10ff38f11f7b6f3cdc000a753e0fe4 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.tesst_1___tesst_1____sicky__header__state.update_scroll_y", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center", ["justifyContent"] : "top", ["backgroundColor"] : "rgba(255, 246, 232,0.8)", ["minHeight"] : "100vh", ["width"] : "100vw", ["height"] : "100vh", ["overflowX"] : "hidden", ["overflowY"] : "scroll" }),direction:"column",id:"my_vstack",onScroll:on_scroll_dd10ff38f11f7b6f3cdc000a753e0fe4,ref:ref_my_vstack,gap:"3"},
jsx(Box_c1db6a30ef12b80469408f29b453f379,{},)
,jsx(
RadixThemesBox,
{css:({ ["height"] : "fit-content", ["width"] : "100vw", ["position"] : "relative", ["alignItems"] : "flex-start" })},
jsx(RadixThemesBox,{css:({ ["height"] : "100%", ["width"] : "100%", ["backgroundSize"] : "cover", ["backgroundPosition"] : "center", ["opacity"] : "0.5", ["position"] : "absolute", ["top"] : "0", ["left"] : "0", ["zIndex"] : "0" })},)
,jsx(
RadixThemesBox,
{css:({ ["zIndex"] : "1", ["position"] : "relative", ["padding"] : "1em", ["alignItems"] : "flex-start", ["justifyContent"] : "flex-start", ["height"] : "100%", ["width"] : "100%" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center", ["justifyContent"] : "center" }),direction:"column",gap:"3"},
jsx(
RadixThemesFlex,
{css:({ ["width"] : "100%", ["justifyContent"] : "center", ["alignItems"] : "center" })},
jsx(
RadixThemesText,
{as:"p",css:({ ["fontWeight"] : "bold", ["color"] : "white", ["textAlign"] : "center", ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS" }),size:"9"},
"Welcome to Lunch Hero!"
,),jsx(
RadixThemesBox,
{css:({ ["position"] : "relative", ["height"] : "200px", ["width"] : "200px" })},
jsx(Img_5d46ab6f7f0fd2f78ff55b03fe6002e7,{},)
,),),jsx(
RadixThemesText,
{as:"p",css:({ ["fontSize"] : "md", ["color"] : "white", ["textAlign"] : "center", ["borderRadius"] : "10px", ["backgroundColor"] : "rgba(0, 0, 0, 0.4)", ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS", ["padding"] : "1em", ["marginTop"] : "-3em" })},
"We\u2019re developing a convenient lunchbox service designed to take the stress out of daily school lunch prep for busy parents while making healthy eating fun and appealing for kids! Our goal is to deliver fresh, nutritious, and allergen-aware lunches that kids genuinely enjoy; served with a playful twist to help reduce the chances of food coming back uneaten!"
,),),),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center", ["width"] : "100%", ["padding"] : "2em" }),direction:"column",id:"target",ref:ref_target,gap:"3"},
jsx(
RadixThemesText,
{as:"p"},
"Test Body"
,),),)
  )
}

export function Box_c1db6a30ef12b80469408f29b453f379 () {
  
  const reflex___state____state__tesst_1___tesst_1____sicky__header__state = useContext(StateContexts.reflex___state____state__tesst_1___tesst_1____sicky__header__state)





  
  return (
    jsx(
RadixThemesBox,
{css:({ ["position"] : "fixed", ["top"] : "0", ["width"] : "100%", ["height"] : "80px", ["overflow"] : "hidden", ["padding"] : "1em", ["backgroundColor"] : ((reflex___state____state__tesst_1___tesst_1____sicky__header__state.scroll_y > 10) ? "rgba(255, 242, 214, 0.7)" : "transparent"), ["transition"] : "background-color 0.1s ease", ["zIndex"] : "1000", ["boxShadow"] : ((reflex___state____state__tesst_1___tesst_1____sicky__header__state.scroll_y > 10) ? "0 2px 6px rgba(0,0,0,0.2)" : "none") })},
jsx(
RadixThemesFlex,
{css:({ ["top"] : "0", ["width"] : "100%" })},
jsx(Img_20af87e7a058b3ff0067e50f73125a2d,{},)
,jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},)
,jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "flex" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "flex" }), ["@media screen and (min-width: 80em)"] : ({ ["display"] : "flex" }), ["marginTop"] : "15px" }),direction:"row",gap:"4"},
jsx(
RadixThemesText,
{as:"p",css:({ ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) })},
"Order"
,),jsx(
RadixThemesText,
{as:"p",css:({ ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) })},
"How It Works"
,),jsx(
RadixThemesText,
{as:"p",css:({ ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) })},
"On the Menu"
,),jsx(
RadixThemesButton,
{css:({ ["backgroundColor"] : "rgb(161, 169, 130)", ["fontFamily"] : "Comic Sans MS", ["--default-font-family"] : "Comic Sans MS", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) })},
"Sign Up / Log In"
,),jsx("img",{css:({ ["width"] : "60px", ["marginTop"] : "-10px", ["&:hover"] : ({ ["transform"] : "scale(1.1)", ["transition"] : "transform 0.2s" }) }),src:"/Shopping Cart.png"},)
,),jsx(Drawer__root_5dc6a97cbb623ed010e78227f740428e,{},)
,),)
  )
}

export default function Component() {
    




  return (
    jsx(
Fragment,
{},
jsx(Flex_25009d6dee37281ac7f1b43db42bc00a,{},)
,jsx(
NextHead,
{},
jsx(
"title",
{},
"Welcome Page"
,),jsx("meta",{content:"favicon.ico",property:"og:image"},)
,),)
  )
}
