import { InputWidget, InputWidgetView } from "@bokehjs/models/widgets/input_widget";
import { StyleSheetLike } from "@bokehjs/core/dom";
import { ButtonType } from "@bokehjs/core/enums";
import * as p from "@bokehjs/core/properties";
export declare class FileDownloadView extends InputWidgetView {
    model: FileDownload;
    anchor_el: HTMLAnchorElement;
    _downloadable: boolean;
    _click_listener: any;
    _prev_href: string | null;
    _prev_download: string | null;
    protected input_el: HTMLInputElement;
    connect_signals(): void;
    render(): void;
    stylesheets(): StyleSheetLike[];
    _increment_clicks(): void;
    _handle_click(): void;
    _make_link_downloadable(): void;
    _update_href(): void;
    _update_download(): void;
    _update_label(): void;
    _update_button_style(): void;
    set_disabled(): void;
}
export declare namespace FileDownload {
    type Attrs = p.AttrsOf<Props>;
    type Props = InputWidget.Props & {
        auto: p.Property<boolean>;
        button_type: p.Property<ButtonType>;
        clicks: p.Property<number>;
        data: p.Property<string | null>;
        embed: p.Property<boolean>;
        label: p.Property<string>;
        filename: p.Property<string | null>;
        _transfers: p.Property<number>;
    };
}
export interface FileDownload extends FileDownload.Attrs {
}
export declare class FileDownload extends InputWidget {
    properties: FileDownload.Props;
    constructor(attrs?: Partial<FileDownload.Attrs>);
    static __module__: string;
}
