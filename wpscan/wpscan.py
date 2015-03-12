#! /usr/bin/env python
#coding=utf-8
#write youstar
#vuln db from http://www.0x.cn/src/wp-vul.log
import sys,urllib2,time,datetime
from urllib2 import URLError

vuln =["wp-content/plugins/ajax-category-dropdown/includes/dhat-ajax-cat-dropdown-request.php",
"wp-content/plugins/php_speedy_wp/libs/php_speedy/view/admin_container.php",
"wp-admin/edit-tags.php",
"wp-admin/link-manager.php",
"wp-content/plugins/wptouch/wptouch.php",
"wp-content/plugins/is-human/engine.php",
"wp-content/plugins/editormonkey/fckeditor/editor/filemanager/upload/test.html",
"wp-content/plugins/sermon-browser/sermon.php",
"wp-content/plugins/backwpup/wp_xml_export.php",
"wp-content/plugins/flash-album-gallery/lib/hitcounter.php",
"wp-content/plugins/wp-custom-pages/wp-download.php",
"wp-content/plugins/old-post-spinner/logview.php",
"wp-content/plugins/jquery-mega-menu/skin.php",
"wp-content/plugins/iwant-one-ihave-one/updateAJAX.php",
"wp-content/plugins/forum-server/feed.php",
"wp-content/plugins/relevanssi/relevanssi.php",
"wp-content/plugins/gigpress/gigpress.php",
"wp-content/plugins/comment-rating/comment-rating-options.php",
"wp-content/plugins/zvote/zvote.php",
"wp-content/plugins/user-photo/user-photo.php",
"wp-content/plugins/enable-media-replace/upload.php",
"wp-content/plugins/mingle-forum/feed.php",
"wp-admin/post.php",
"wp-content/plugins/accept-signups/accept-signups_submit.php",
"wp-includes/comment.php",
"wp-content/plugins/event-registration/event_regis.php",
"wp-content/plugins/events-manager-extended/events-manager.php",
"wp-content/plugins/nextgen-smooth-gallery/nggSmoothFrame.php",
"wp-content/plugins/firestats/php/tools/get_config.php",
"myLDlinker.php",
"wp-content/plugins/simple-forum/sf-header-forum.php",
"wp-content/plugins/cimy-counter/cimy_counter.php",
"wp-content/plugins/nextgen-gallery/nggallery.php",
"wp-content/plugins/cpl/cplphoto.php",
"wp-content/plugins/events-calendar/events-calendar.php",
"wp-content/plugins/pyrmont-v2/index.php",
"wp-content/plugins/ImageManager/manager.php",
"wp-content/plugins/wp-cumulus/wp-cumulus.php",
"wp-includes/wpmu-functions.php",
"wp-content/plugins/wp-syntax/test/index.php",
"wp-content/plugins/my-category-order/mycategoryorder.php",
"wp-content/plugins/related-sites/BTE_RW_webajax.php",
"wp-content/plugins/dm-albums/dm-albums.php",
"wp-content/plugins/dm-albums/template/album.php",
"wp-content/plugins/photoracer/viewimg.php",
"wp-content/plugins/wp-lytebox/main.php",
"wp-content/plugins/fmoblog.php",
"wp-content/plugins/wp-forum/forum_feed.php",
"wp-content/plugins/page-flip-image-gallery/books/getConfig.php",
"wp-content/plugins/wp-shopping-cart/image_processing.php",
"mediaHolder.php",
"wp-content/plugins/st_newsletter/stnl_iframe.php",
"wp-content/plugins/downloads-manager/upload.php",
"wp-content/plugins/wpSS/ss_load.php",
"wp-content/plugins/wp-download/wp-download.php",
"wp-content/plugins/sniplets/modules/syntax_highlight.php",
"wp-content/plugins/wp-photo-album/wppa.php",
"wp-content/plugins/simple-forum/sf-includes.php",
"wp-content/plugins/simple-forum/sf-includes.php",
"wp-content/plugins/st_newsletter/shiftthis-preview.php",
"wp-content/plugins/wordspew/wordspew-rss.php",
"wp-content/plugins/dmsguestbook/dmsguestbook.php",
"wp-content/plugins/wassup/spy.php",
"wp-content/plugins/wp-adserve/adclick.php",
"wp-content/plugins/fgallery/fim_rss.php",
"wp-content/plugins/wp-cal/functions/editevent.php",
"wp-content/plugins/wp-forum/wp-forum.php",
"wp-content/plugins/wp-filemanager/ajaxfilemanager/ajaxfilemanager.php",
"wp-content/plugins/pictpress/resize.php",
"wp-content/plugins/BackUp/Archive.php",
"wp-content/plugins/myflash/myflash-button.php",
"wp-content/plugins/wordtube/wordtube-button.php",
"wp-content/plugins/wp-table/js/wptable-button.php",
"wp-content/plugins/mygallery/mygallery.php",
"wp-content/plugins/Enigma2.php",
"wp-content/plugins/fckeditor-for-wordpress-plugin/filemanager/browser/default/browser.html",
"wp-content/themes/THEME/timthumb.php",
"wp-content/plugins/wp-e-commerce/wpsc-theme/functions/wpsc-user_log_functions.php",
"wp-content/plugins/ungallery/source_vuln.php",
"wp-content/plugins/wp-menu-creator/updateSortOrder.php",
"wp-content/plugins/mm-duplicate/mm-duplicate.php",
"wp-content/plugins/sendit/submit.php",
"wp-content/plugins/photoracer/viewimg.php",
"wp-content/plugins/easy-comment-uploads/upload-form.php",
"wp-content/plugins/allow-php-in-posts-and-pages/alter.php",
"wp-content/plugins/ajaxgallery/utils/list.php",
"wp-content/plugins/wpforum/sendmail.php",
"wp-content/plugins/wp-ds-faq/ajax.php",
"wp-content/plugins/easy-contact-form-lite/requests/sort_row.request.php",
"wp-content/plugins/wp-symposium/uploadify/get_profile_avatar.php",
"wp-content/plugins/contus-hd-flv-player/process-sortable.php",
"wp-content/plugins/file-groups/download.php",
"wp-content/plugins/wp-css/wp-css-compress.php",
"wp-content/plugins/mm-forms-community/includes/edit_details.php",
"wp-content/plugins/js-appointment/searchdata.php",
"wp-content/plugins/oqey-headers/oqey_settings.php",
"wp-content/plugins/fbpromotions/fbActivate.php",
"wp-content/plugins/profiles/library/bio-img.php",
"wp-content/plugins/evarisk/include/ajax.php",
"wp-content/plugins/mystat/mystat.php",
"wp-content/plugins/sh-slideshow/ajax.php",
"wp-content/plugins/copyright-licensing-tools/icopyright_xml.php",
"wp-content/plugins/advertizer/click_ads.php",
"wp-content/plugins/event-registration/event_registration_export.php",
"wp-content/plugins/crawlrate-tracker/sbtracking-chart-data.php",
"wp-content/plugins/wp-audio-gallery-playlist/playlist.php",
"wp-content/plugins/yolink-search/includes/bulkcrawl.php",
"wp-content/plugins/pure-html/alter.php",
"wp-content/plugins/couponer/print-coupon.php",
"wp-content/plugins/grapefile/grapeupload.php",
"wp-content/plugins/image-gallery-with-slideshow/upload-file.php",
"wp-content/plugins/wordpress-donation-plugin-with-goals-and-paypal-ipn-by-nonprofitcmsorg/exporttocsv.php",
"wp-content/plugins/wp-bannerize/ajax_clickcounter.php",
"wp-content/plugins/search-autocomplete/includes/tags.php",
"wp-content/plugins/videowhisper-video-presentation/vp/c_status.php",
"wp-content/plugins/facebook-opengraph-meta-plugin/all_meta.php",
"wp-content/plugins/zotpress/zotpress.rss.php",
"wp-content/plugins/oqey-gallery/getimages.php",
"wp-content/plugins/tweet-old-post/tweet-old-post.php",
"wp-content/plugins/post-highlights/ajax/ph_settings.php",
"wp-content/plugins/knr-author-list-widget/knrAuthorListCustomSortSave.php",
"wp-content/plugins/scormcloud/ajax.php",
"wp-content/plugins/eventify/php/ajax/fetcheventdetails.php",
"wp-content/plugins/paid-downloads/download.php",
"wp-content/plugins/community-events/tracker.php",
"wp-content/plugins/1-flash-gallery/upload.php",
"wp-content/plugins/wp-filebase/wpfb-ajax.php",
"wp-content/plugins/a-to-z-category-listing/post_retrive_ajax.php",
"wp-content/plugins/events-2/"
"wp-content/plugins/tune-library/tune-library-ajax.php",
"wp-content/plugins/forum-server/wpf-insert.php",
"wp-content/plugins/wp-e-commerce/wp-shopping-cart.php",
"wp-content/plugins/count-per-day/notes.php",
"wp-content/plugins/filedownload/download.php",
"wp-content/plugins/thecartpress/checkout/CheckoutEditor.php",
"wp-content/plugins/allwebmenus-wordpress-menu-plugin/actions.php",
"wp-content/plugins/wpeasystats/export.php",
"wp-content/plugins/annonces/includes/lib/photo/uploadPhoto.php",
"wp-content/plugins/livesig/livesig-ajax-backend.php",
"wp-content/plugins/disclosure-policy-plugin/functions/action.php",
"wp-content/plugins/mailz/lists/config/config.php",
"wp-content/plugins/zingiri-web-shop/fws/ajax/init.inc.php",
"wp-content/plugins/mini-mail-dashboard-widgetwp-mini-mail.php",
"wp-content/plugins/relocate-upload/relocate-upload.php",
"wp-content/plugins/category-grid-view-gallery/includes/timthumb.php",
"wp-content/plugins/auto-attachments/thumb.php",
"wp-content/plugins/wp-marketplace/libs/timthumb.php",
"wp-content/plugins/dp-thumbnail/timthumb/timthumb.php",
"wp-content/plugins/vk-gallery/lib/timthumb.php",
"wp-content/plugins/rekt-slideshow/picsize.php",
"wp-content/plugins/cac-featured-content/timthumb.php",
"wp-content/plugins/rent-a-car/libs/timthumb.php",
"wp-content/plugins/lisl-last-image-slider/timthumb.php",
"wp-content/plugins/islidex/js/timthumb.php",
"wp-content/plugins/kino-gallery/timthumb.php",
"wp-content/plugins/cms-pack/timthumb.php",
"wp-content/plugins/a-gallery/timthumb.php",
"wp-content/plugins/category-list-portfolio-page/scripts/timthumb.php",
"wp-content/plugins/really-easy-slider/inc/thumb.php",
"wp-content/plugins/verve-meta-boxes/tools/timthumb.php",
"wp-content/plugins/user-avatar/user-avatar-pic.php",
"wp-content/plugins/extend-wordpress/helpers/timthumb/image.php",
"wp-content/plugins/link-library/link-library-ajax.php",
"wp-content/plugins/adrotate/adrotate-out.php",
"wp-content/plugins/cevhershare/cevhershare-admin.php",
"wp-content/plugins/mingle-forum/wpf-insert.php",
"wp-content/plugins/wp-bannerize/ajax_sorter.php",
"wp-content/plugins/wp-spamfree/js/wpsf-js.php",
"wp-content/plugins/gd-star-rating/export.php",
"wp-content/plugins/contact-form-wordpress/easy-form.class.php",
"wp-content/plugins/wp-photo-album-plus/wppa-functions.php",
"wp-content/plugins/backwpup/job/wp_export_generate.php",
"wp-content/themes/classipress/index.php",
"wp-content/plugins/wp-glossary/ajax.php",
"wp-content/plugins/zingiri-web-shop/fws/addons/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajax_save_name.php",
"wp-content/plugins/adrotate/adrotate-out.php",
"wp-content/plugins/jetpack/modules/sharedaddy.php",
"wp-content/plugins/universal-post-manager/bycat.php",
"wp-content/plugins/mailz/lists/dl.php",
"wp-content/plugins/pay-with-tweet.php/pay.php",
"wp-content/plugins/age-verification/age-verification.php",
"wp-content/plugins/wp-autoyoutube/modules/index.php",
"wp-content/plugins/count-per-day/download.php",
"wp-content/plugins/ucan-post/"
"wp-content/plugins/kish-guest-posting/uploadify/scripts/uploadify.php",
"wp-content/plugins/zingiri-web-shop/zing.inc.php",
"wp-content/plugins/wp-property/third-party/uploadify/uploadify.php",
"wp-content/plugins/wpmarketplace/uploadify/uploadify.php",
"wp-content/plugins/store-locator-le/core/load_wp_config.php",
"wp-content/plugins/html5avmanager/lib/uploadify/custom.php",
"wp-content/plugins/foxypress/uploadify/uploadify.php",
"wp-content/plugins/asset-manager/upload.php",
"wp-content/plugins/font-uploader/font-upload.php",
"wp-content/plugins/mm-forms-community/includes/doajaxfileupload.php",
"wp-content/plugins/gallery-plugin/upload/php.php",
"wp-content/plugins/front-end-upload/upload.php",
"wp-content/plugins/omni-secure-files/plupload/examples/upload.php",
"wp-content/plugins/wpstorecart/php/upload.php",
"wp-content/plugins/tinymce-thumbnail-gallery/php/download-image.php",
"wp-content/plugins/thinkun-remind/exportData.php",
"wp-content/plugins/simple-download-button-shortcode/simple-download-button_dl.php",
"wp-content/plugins/rbxgallery/uploader.php",
"wp-content/plugins/plugin-newsletter/preview.php",
"wp-content/plugins/pica-photo-gallery/picadownload.php",
"wp-content/plugins/easy-contact-forms-exporter/downloadcsv.php",
"wp-content/plugins/front-file-manager/upload.php",
"wp-content/plugins/content-flow3d/"
"wp-content/plugins/custom-content-type-manager/upload_form.php",
"wp-content/plugins/drag-drop-file-uploader/dnd-upload.php",
"wp-content/plugins/mac-dock-gallery/upload-file.php",
"wp-content/plugins/pica-photo-gallery/picaPhotosResize.php",
"wp-content/plugins/sfbrowser/connectors/php/sfbrowser.php",
"wp-content/plugins/topquark/lib/js/fancyupload/showcase/batch/script.php",
"wp-content/plugins/user-meta/framework/helper/uploader.php",
"wp-content/plugins/wp-gpx-maps/wp-gpx-maps_admin_tracks.php",
"wp-content/plugins/deans-fckeditor-with-pwwangs-code-plugin-for-wordpress/filemanager/connectors/test.html"
"wp-content/plugins/buddypress/bp-loader.php",
"wp-content/plugins/mowpop/submit.php",
"wp-content/plugins/taggator/taggator.php",
"wp-content/plugins/wp-insert/fckeditor/editor/filemanager/browser/default/frmupload.html"
"advanced-search.php",
"wp-content/plugins/email-before-download/email-before-download.php",
"wp-content/themes/3dcubes/index.php",
"wp-content/plugins/HT-Poi/file_upload.php",
"wp-content/plugins/wp-easy-gallery/wp-easy-gallery.php",
"wp-content/plugins/imagedrop/ImageDrop.php",
"wp-content/plugins/ss-downloads/services/getfile.php",
"wp-content/plugins/custom-background/uploadify/uploadify.php",
"wp-content/plugins/placester/js/uploadify/uploadify.php",
"wp-content/themes/photocrati-theme/admin/upload_edit.php",
"wp-content/plugins/katalyst-timthumb/timthumb.php",
"wp-content/plugins/wp-automatic/inc/csv.php",
"wp-content/plugins/arcadepress/php/upload.php",
"wp-content/plugins/lb-mixed-slideshow/libs/uploadify/upload.php",
"wp-content/plugins/wp-imagezoom/download.php",
"wp-content/plugins/lim4wp/includes/upload.php",
"wp-content/themes/famous/megaframe/megapanel/inc/upload.php",
"wp-content/themes/deep-blue/megaframe/megapanel/inc/upload.php",
"wp-content/plugins/organizer/page/users.php",
"wp-content/plugins/super-capcha/super-capcha.php",
"wp-content/plugins/testimonials/testimonials.php"]

vulninfo = ["http://www.exploit-db.com/exploits/17207/",
"http://www.exploit-db.com/exploits/16273/",
"http://www.exploit-db.com/exploits/17465/",
"http://www.exploit-db.com/exploits/17465/",
"http://www.exploit-db.com/exploits/17423/ : http://www.exploit-db.com/exploits/18039/",
"http://www.exploit-db.com/exploits/17299/",
"http://www.exploit-db.com/exploits/17284/",
"http://www.exploit-db.com/exploits/17214/",
"http://www.exploit-db.com/exploits/17056/",
"http://www.exploit-db.com/exploits/16947/",
"http://www.exploit-db.com/exploits/17119/",
"http://www.exploit-db.com/exploits/16251/",
"http://www.exploit-db.com/exploits/16250/",
"http://www.exploit-db.com/exploits/16236/",
"http://www.exploit-db.com/exploits/16235/",
"http://www.exploit-db.com/exploits/16233/",
"http://www.exploit-db.com/exploits/16232/",
"http://www.exploit-db.com/exploits/16221/",
"http://www.exploit-db.com/exploits/16218/",
"http://www.exploit-db.com/exploits/16181/",
"http://www.exploit-db.com/exploits/16144/",
"http://www.exploit-db.com/exploits/15943/ : http://www.1337day.com/exploits/17826",
"http://www.exploit-db.com/exploits/15858/",
"http://www.exploit-db.com/exploits/15808/",
"http://www.exploit-db.com/exploits/15684/",
"http://www.exploit-db.com/exploits/15513/",
"http://www.exploit-db.com/exploits/14923/",
"http://www.exploit-db.com/exploits/14541/",
"http://www.exploit-db.com/exploits/14308/",
"http://www.exploit-db.com/exploits/14441/",
"http://www.exploit-db.com/exploits/14198/",
"http://www.exploit-db.com/exploits/14057/",
"http://www.exploit-db.com/exploits/12098/",
"http://www.exploit-db.com/exploits/11458/",
"http://www.exploit-db.com/exploits/10929/",
"http://www.exploit-db.com/exploits/10535/",
"http://www.exploit-db.com/exploits/10325/",
"http://www.exploit-db.com/exploits/10228/",
"http://www.exploit-db.com/exploits/10090/",
"http://www.exploit-db.com/exploits/9431/",
"http://www.exploit-db.com/exploits/9150/",
"http://www.exploit-db.com/exploits/9054/",
"http://www.exploit-db.com/exploits/9048/",
"http://www.exploit-db.com/exploits/9043/",
"http://www.exploit-db.com/exploits/8961/",
"http://www.exploit-db.com/exploits/8791/",
"http://www.exploit-db.com/exploits/8229/",
"http://www.exploit-db.com/exploits/7738/",
"http://www.exploit-db.com/exploits/7543/",
"http://www.exploit-db.com/exploits/6867/",
"http://www.exploit-db.com/exploits/6842/",
"http://www.exploit-db.com/exploits/6777/",
"http://www.exploit-db.com/exploits/6127/",
"http://www.exploit-db.com/exploits/5486/",
"http://www.exploit-db.com/exploits/5326/",
"http://www.exploit-db.com/exploits/5194/",
"http://www.exploit-db.com/exploits/5135/",
"http://www.exploit-db.com/exploits/5126/",
"http://www.exploit-db.com/exploits/5127/",
"http://www.exploit-db.com/exploits/5053/",
"http://www.exploit-db.com/exploits/5039/",
"http://www.exploit-db.com/exploits/5035/",
"http://www.exploit-db.com/exploits/5017/",
"http://www.exploit-db.com/exploits/5013/",
"http://www.exploit-db.com/exploits/4993/",
"http://www.exploit-db.com/exploits/4992/",
"http://www.exploit-db.com/exploits/4939/",
"http://www.exploit-db.com/exploits/4844/",
"http://www.exploit-db.com/exploits/4695/",
"http://www.exploit-db.com/exploits/4593/",
"http://www.exploit-db.com/exploits/3828/",
"http://www.exploit-db.com/exploits/3825/",
"http://www.exploit-db.com/exploits/3824/",
"http://www.exploit-db.com/exploits/3814/",
"http://www.exploit-db.com/exploits/3051/",
"http://www.1337day.com/exploits/16488",
"http://www.exploit-db.com/exploits/17602/",
"http://www.exploit-db.com/exploits/17613/ : http://packetstormsecurity.org/files/view/103724/wpecommerce-xss.txt",
"http://www.exploit-db.com/exploits/17704/",
"http://www.exploit-db.com/exploits/17689/",
"http://www.exploit-db.com/exploits/17707/",
"http://www.exploit-db.com/exploits/17716/",
"http://www.exploit-db.com/exploits/17720/ : http://www.exploit-db.com/exploits/17731/",
"http://www.1337day.com/exploits/16720",
"http://www.1337day.com/exploits/16718",
"http://www.1337day.com/exploits/16716",
"http://www.1337day.com/exploits/16711",
"http://www.1337day.com/exploits/16710",
"http://www.1337day.com/exploits/16708",
"http://www.1337day.com/exploits/16707 : http://www.1337day.com/exploits/18565",
"http://www.1337day.com/exploits/16706",
"http://www.1337day.com/exploits/16705",
"http://www.1337day.com/exploits/16756",
"http://www.exploit-db.com/exploits/17725/",
"http://www.exploit-db.com/exploits/17724/",
"http://www.exploit-db.com/exploits/17730/",
"http://www.exploit-db.com/exploits/17737/",
"http://www.exploit-db.com/exploits/17739/",
"http://www.exploit-db.com/exploits/17738/",
"http://www.exploit-db.com/exploits/17740/",
"http://www.exploit-db.com/exploits/17748/",
"http://www.exploit-db.com/exploits/17749/",
"http://www.exploit-db.com/exploits/17750/",
"http://www.exploit-db.com/exploits/17751/",
"http://www.exploit-db.com/exploits/17755/",
"http://www.exploit-db.com/exploits/17756/",
"http://www.exploit-db.com/exploits/17757/",
"http://www.exploit-db.com/exploits/17758/",
"http://www.exploit-db.com/exploits/17759/",
"http://www.exploit-db.com/exploits/17760/",
"http://www.exploit-db.com/exploits/17761/",
"http://www.exploit-db.com/exploits/17763/",
"http://www.exploit-db.com/exploits/17764/",
"http://www.exploit-db.com/exploits/17767/",
"http://www.exploit-db.com/exploits/17771/",
"http://www.exploit-db.com/exploits/17773/",
"http://www.exploit-db.com/exploits/17778/",
"http://www.exploit-db.com/exploits/17779/",
"http://www.exploit-db.com/exploits/17789/",
"http://www.exploit-db.com/exploits/17790/",
"http://www.exploit-db.com/exploits/17791/",
"http://www.exploit-db.com/exploits/17793/",
"http://www.exploit-db.com/exploits/17794/",
"http://www.exploit-db.com/exploits/17797/",
"http://www.exploit-db.com/exploits/17798/",
"http://www.exploit-db.com/exploits/17801/",
"http://www.exploit-db.com/exploits/17808/",
"http://www.exploit-db.com/exploits/17809/",
"http://www.exploit-db.com/exploits/17814/",
"http://www.exploit-db.com/exploits/17816/",
"http://www.exploit-db.com/exploits/17828/",
"http://www.exploit-db.com/exploits/17832/",
"http://www.exploit-db.com/exploits/17857/",
"http://www.exploit-db.com/exploits/17858/",
"http://www.exploit-db.com/exploits/17860/ : http://www.1337day.com/exploits/18018",
"http://www.exploit-db.com/exploits/17861/",
"http://www.exploit-db.com/exploits/17862/",
"http://www.exploit-db.com/exploits/17863/",
"http://www.exploit-db.com/exploits/17864/",
"http://www.exploit-db.com/exploits/17865/",
"http://www.exploit-db.com/exploits/17866/",
"http://www.exploit-db.com/exploits/17867/ : http://www.1337day.com/exploits/18015",
"http://www.exploit-db.com/exploits/17868/",
"http://www.exploit-db.com/exploits/17869/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17872/",
"http://www.exploit-db.com/exploits/17887/",
"http://www.exploit-db.com/exploits/17888/",
"http://www.exploit-db.com/exploits/17891/",
"http://www.exploit-db.com/exploits/17894/ : http://www.1337day.com/exploits/17826",
"http://www.exploit-db.com/exploits/17906/",
"http://www.exploit-db.com/exploits/17970/",
"http://www.exploit-db.com/exploits/17973/",
"http://www.exploit-db.com/exploits/17980/",
"http://www.exploit-db.com/exploits/17983/",
"http://www.exploit-db.com/exploits/17987/",
"http://www.exploit-db.com/exploits/18053/",
"http://www.exploit-db.com/exploits/18055/",
"http://www.exploit-db.com/exploits/18111/ : http://www.1337day.com/exploits/18015",
"http://www.exploit-db.com/exploits/18114/",
"http://www.exploit-db.com/exploits/18126/",
"http://www.exploit-db.com/exploits/18231/",
"http://www.exploit-db.com/exploits/18276/",
"http://www.exploit-db.com/exploits/18330/",
"http://www.exploit-db.com/exploits/18350/",
"http://www.exploit-db.com/exploits/18353/",
"http://www.exploit-db.com/exploits/18355/",
"http://www.exploit-db.com/exploits/18390/",
"http://www.exploit-db.com/exploits/18412/",
"http://www.exploit-db.com/exploits/18787/ : http://www.exploit-db.com/exploits/18806/ : http://www.1337day.com/exploits/18015",
"http://www.exploit-db.com/exploits/18987/",
"http://www.exploit-db.com/exploits/18988/",
"http://www.exploit-db.com/exploits/18989/",
"http://www.exploit-db.com/exploits/18990/",
"http://www.exploit-db.com/exploits/18991/ : http://www.exploit-db.com/exploits/19100/",
"http://www.exploit-db.com/exploits/18993/",
"http://www.exploit-db.com/exploits/18994/",
"http://www.exploit-db.com/exploits/18997/ : http://www.1337day.com/exploits/18471",
"http://www.exploit-db.com/exploits/18998/",
"http://www.exploit-db.com/exploits/19008/",
"http://www.exploit-db.com/exploits/19009/",
"http://www.exploit-db.com/exploits/19023/",
"http://www.exploit-db.com/exploits/19022/",
"http://www.exploit-db.com/exploits/19021/",
"http://www.exploit-db.com/exploits/19020/",
"http://www.exploit-db.com/exploits/19019/",
"http://www.exploit-db.com/exploits/19018/",
"http://www.exploit-db.com/exploits/19016/",
"http://www.exploit-db.com/exploits/19013/",
"http://www.exploit-db.com/exploits/19012/",
"http://www.exploit-db.com/exploits/19036/",
"http://www.exploit-db.com/exploits/19058/",
"http://www.exploit-db.com/exploits/19057/",
"http://www.exploit-db.com/exploits/19056/",
"http://www.exploit-db.com/exploits/19055/",
"http://www.exploit-db.com/exploits/19054/",
"http://www.exploit-db.com/exploits/19053/",
"http://www.exploit-db.com/exploits/19052/",
"http://www.exploit-db.com/exploits/19050/",
"http://www.1337day.com/exploits/17860",
"http://www.1337day.com/exploits/17906",
"http://www.1337day.com/exploits/17931",
"http://www.1337day.com/exploits/17992",
"http://www.1337day.com/exploits/17994",
"http://www.1337day.com/exploits/18012",
"http://www.1337day.com/exploits/18049",
"http://www.1337day.com/exploits/18371",
"http://www.1337day.com/exploits/18444",
"http://www.1337day.com/exploits/18496",
"http://www.1337day.com/exploits/18529",
"http://www.1337day.com/exploits/18530",
"http://www.1337day.com/exploits/18566",
"http://www.1337day.com/exploits/18567",
"http://www.1337day.com/exploits/18586",
"http://www.1337day.com/exploits/18589",
"http://www.exploit-db.com/exploits/19187/",
"http://www.1337day.com/exploits/18668",
"http://www.1337day.com/exploits/18684",
"http://www.1337day.com/exploits/18685",
"http://www.1337day.com/exploits/18686",
"http://www.1337day.com/exploits/18687",
"http://www.1337day.com/exploits/18688",
"http://www.1337day.com/exploits/18133",
"http://www.exploit-db.com/exploits/17728/",
"http://www.exploit-db.com/exploits/17729/"]

def wpscanhelp():
    print "\n|-------------------------------------------------------------  |"
    print "|      youstar[@]foxmail[dot]com  v1.0                          |"
    print "|      6/2012      wpscan.py                                    |"
    print "|      --simple wordpress vulnerability  scanner--              |"
    print "| Usage:    swpscan.py  <site+dir>                              |"
    print "| Example:  swpscan.py  www.site.com                            |"
    print "|---------------------------------------------------------------|\n"
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        wpscanhelp()
    findvuln = []
    findvulninfo = []
    host = sys.argv[1].replace("http://","").rsplit("/",1)[0]
    if host[-1] != "/":
        host = host+"/"
    print "\n[+] Site:",host
    print "[+] vuln Loaded:",len(vuln)
    ##begin
    starttime = datetime.datetime.now()
    for i in range(len(vuln)):
        time.sleep(2) #Change this if needed
        ivuln = "http://"+ host + vuln[i].replace("\n","")  
        print "[+] Trying:",i,ivuln.replace("\n","")
        header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request(url= ivuln,headers = header)
        try:
            ihttp = urllib2.urlopen(req)
            print "[+] Find:%s"%(ivuln)
            print "vuln info link:%s"%(vulninfo[i])
            findvuln.append(ivuln)
            findvulninfo.append(vulninfo[i])
        except:   
            pass
    ##end
    endtime = datetime.datetime.now()
    print "Spent time:%s s"%((endtime - starttime).seconds)
    print "Total find vuln:%s"%(len(findvuln))
    print "Detail................."
    print "++++++++++++++++++++++++++++++++++++++++++++++++"
    for i in range(len(findvuln)):
        print "[+] Find:%s"%(findvuln[i])
        print "vuln info link:%s"%(findvulninfo[i])
        
