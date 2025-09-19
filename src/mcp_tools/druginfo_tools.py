from typing import Optional, Dict, Any

from mcp.server.fastmcp import FastMCP

from src.druginfo import (
    list_main_ingredient,
    get_main_ingredient_by_code,
    list_product,
    get_product_by_code,
    UnauthorizedError,
    DrugInfoError,
    list_main_ingredient_drug_effect,
    get_main_ingredient_drug_effect_by_id,
    list_main_ingredient_drug_kind,
    list_main_ingredient_guide_a4,
    list_main_ingredient_guide_a5,
    list_main_ingredient_picto,
    get_main_ingredient_picto_by_code,
    list_product_edicode,
    # non-GET
    create_drug_effect,
    merge_drug_effect,
    update_drug_effect,
    delete_drug_effect,
    create_drug_kind,
    merge_drug_kind,
    update_drug_kind,
    delete_drug_kind,
    create_guide_a4,
    merge_guide_a4,
    update_guide_a4,
    delete_guide_a4,
    create_guide_a5,
    merge_guide_a5,
    update_guide_a5,
    delete_guide_a5,
    create_main_ingredient,
    bulk_main_ingredient,
    update_main_ingredient,
    delete_main_ingredient,
    delete_main_ingredient_cache,
    update_main_ingredient_picto,
    create_product,
    update_product,
    export_product,
    delete_product,
)
from src.mcp_tools.auth_tools import _try_auto_login


def register_druginfo_tools(mcp: FastMCP) -> None:
    @mcp.tool(name="druginfo_list_main_ingredient")
    def druginfo_list_main_ingredient(
        a4: Optional[bool] = None,
        a4Off: Optional[bool] = None,
        a5: Optional[bool] = None,
        a5Off: Optional[bool] = None,
        drugkind: Optional[bool] = None,
        drugkindOff: Optional[bool] = None,
        effect: Optional[bool] = None,
        effectOff: Optional[bool] = None,
        showMapped: Optional[bool] = None,
        IngredientCode: Optional[str] = None,
        ingredientNameKor: Optional[str] = None,
        drugKind: Optional[str] = None,
        PageSize: Optional[int] = None,
        Page: Optional[int] = None,
        SortBy: Optional[str] = None,
        # legacy aliases
        q: Optional[str] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
        timeout: int = 15,
    ) -> Dict[str, Any]:
        try:
            return list_main_ingredient(
                a4=a4,
                a4Off=a4Off,
                a5=a5,
                a5Off=a5Off,
                drugkind=drugkind,
                drugkindOff=drugkindOff,
                effect=effect,
                effectOff=effectOff,
                showMapped=showMapped,
                IngredientCode=IngredientCode,
                ingredientNameKor=ingredientNameKor,
                drugKind=drugKind,
                PageSize=PageSize,
                Page=Page,
                SortBy=SortBy,
                q=q,
                page=page,
                size=size,
                timeout=int(timeout),
            )
        except UnauthorizedError:
            _try_auto_login(timeout)
            return list_main_ingredient(
                a4=a4,
                a4Off=a4Off,
                a5=a5,
                a5Off=a5Off,
                drugkind=drugkind,
                drugkindOff=drugkindOff,
                effect=effect,
                effectOff=effectOff,
                showMapped=showMapped,
                IngredientCode=IngredientCode,
                ingredientNameKor=ingredientNameKor,
                drugKind=drugKind,
                PageSize=PageSize,
                Page=Page,
                SortBy=SortBy,
                q=q,
                page=page,
                size=size,
                timeout=int(timeout),
            )
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_get_main_ingredient_by_code")
    def druginfo_get_main_ingredient_by_code(code: str, timeout: int = 15) -> Dict[str, Any]:
        try:
            return get_main_ingredient_by_code(code=code, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return get_main_ingredient_by_code(code=code, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_list_product")
    def druginfo_list_product(
        crop: Optional[bool] = None,
        cropOff: Optional[bool] = None,
        base64: Optional[bool] = None,
        base64Off: Optional[bool] = None,
        watermark: Optional[bool] = None,
        watermarkOff: Optional[bool] = None,
        confirm: Optional[bool] = None,
        confirmOff: Optional[bool] = None,
        teoulLengthShort: Optional[bool] = None,
        teoulLengthShortOff: Optional[bool] = None,
        teoulLengthLong: Optional[bool] = None,
        teoulLengthLongOff: Optional[bool] = None,
        minCount: Optional[int] = None,
        ProductCode: Optional[str] = None,
        pillName: Optional[str] = None,
        vendor: Optional[str] = None,
        PageSize: Optional[int] = None,
        Page: Optional[int] = None,
        SortBy: Optional[str] = None,
        # legacy aliases
        q: Optional[str] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
        timeout: int = 15,
    ) -> Dict[str, Any]:
        try:
            return list_product(
                crop=crop,
                cropOff=cropOff,
                base64=base64,
                base64Off=base64Off,
                watermark=watermark,
                watermarkOff=watermarkOff,
                confirm=confirm,
                confirmOff=confirmOff,
                teoulLengthShort=teoulLengthShort,
                teoulLengthShortOff=teoulLengthShortOff,
                teoulLengthLong=teoulLengthLong,
                teoulLengthLongOff=teoulLengthLongOff,
                minCount=minCount,
                ProductCode=ProductCode,
                pillName=pillName,
                vendor=vendor,
                PageSize=PageSize,
                Page=Page,
                SortBy=SortBy,
                q=q,
                page=page,
                size=size,
                timeout=int(timeout),
            )
        except UnauthorizedError:
            _try_auto_login(timeout)
            return list_product(
                crop=crop,
                cropOff=cropOff,
                base64=base64,
                base64Off=base64Off,
                watermark=watermark,
                watermarkOff=watermarkOff,
                confirm=confirm,
                confirmOff=confirmOff,
                teoulLengthShort=teoulLengthShort,
                teoulLengthShortOff=teoulLengthShortOff,
                teoulLengthLong=teoulLengthLong,
                teoulLengthLongOff=teoulLengthLongOff,
                minCount=minCount,
                ProductCode=ProductCode,
                pillName=pillName,
                vendor=vendor,
                PageSize=PageSize,
                Page=Page,
                SortBy=SortBy,
                q=q,
                page=page,
                size=size,
                timeout=int(timeout),
            )
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_get_product_by_code")
    def druginfo_get_product_by_code(code: str, timeout: int = 15) -> Dict[str, Any]:
        try:
            return get_product_by_code(code=code, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return get_product_by_code(code=code, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_list_main_ingredient_drug_effect")
    def druginfo_list_main_ingredient_drug_effect(
        edit: Optional[str] = None,
        pageSize: Optional[int] = None,
        page: Optional[int] = None,
        sortBy: Optional[str] = None,
        timeout: int = 15,
    ) -> Dict[str, Any]:
        try:
            return list_main_ingredient_drug_effect(edit=edit, pageSize=pageSize, page=page, sortBy=sortBy, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return list_main_ingredient_drug_effect(edit=edit, pageSize=pageSize, page=page, sortBy=sortBy, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_get_main_ingredient_drug_effect_by_id")
    def druginfo_get_main_ingredient_drug_effect_by_id(effectId: int, timeout: int = 15) -> Dict[str, Any]:
        try:
            return get_main_ingredient_drug_effect_by_id(effect_id=int(effectId), timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return get_main_ingredient_drug_effect_by_id(effect_id=int(effectId), timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_list_main_ingredient_drug_kind")
    def druginfo_list_main_ingredient_drug_kind(edit: Optional[str] = None, pageSize: Optional[int] = None, page: Optional[int] = None, sortBy: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return list_main_ingredient_drug_kind(edit=edit, pageSize=pageSize, page=page, sortBy=sortBy, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return list_main_ingredient_drug_kind(edit=edit, pageSize=pageSize, page=page, sortBy=sortBy, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_list_main_ingredient_guide_a4")
    def druginfo_list_main_ingredient_guide_a4(edit: Optional[str] = None, pageSize: Optional[int] = None, page: Optional[int] = None, sortBy: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return list_main_ingredient_guide_a4(edit=edit, pageSize=pageSize, page=page, sortBy=sortBy, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return list_main_ingredient_guide_a4(edit=edit, pageSize=pageSize, page=page, sortBy=sortBy, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_list_main_ingredient_guide_a5")
    def druginfo_list_main_ingredient_guide_a5(edit: Optional[str] = None, pageSize: Optional[int] = None, page: Optional[int] = None, sortBy: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return list_main_ingredient_guide_a5(edit=edit, pageSize=pageSize, page=page, sortBy=sortBy, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return list_main_ingredient_guide_a5(edit=edit, pageSize=pageSize, page=page, sortBy=sortBy, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_list_main_ingredient_picto")
    def druginfo_list_main_ingredient_picto(IsDeleted: Optional[str] = None, Title: Optional[str] = None, PageSize: Optional[int] = None, Page: Optional[int] = None, SortBy: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return list_main_ingredient_picto(IsDeleted=IsDeleted, Title=Title, PageSize=PageSize, Page=Page, SortBy=SortBy, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return list_main_ingredient_picto(IsDeleted=IsDeleted, Title=Title, PageSize=PageSize, Page=Page, SortBy=SortBy, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_get_main_ingredient_picto_by_code")
    def druginfo_get_main_ingredient_picto_by_code(code: str, timeout: int = 15) -> Dict[str, Any]:
        try:
            return get_main_ingredient_picto_by_code(code=code, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return get_main_ingredient_picto_by_code(code=code, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_list_product_edicode")
    def druginfo_list_product_edicode(ProductCode: Optional[str] = None, EdiCode: Optional[str] = None, PageSize: Optional[int] = None, Page: Optional[int] = None, SortBy: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return list_product_edicode(ProductCode=ProductCode, EdiCode=EdiCode, PageSize=PageSize, Page=Page, SortBy=SortBy, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return list_product_edicode(ProductCode=ProductCode, EdiCode=EdiCode, PageSize=PageSize, Page=Page, SortBy=SortBy, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    # --- Non-GET tool wrappers ---

    @mcp.tool(name="druginfo_create_drug_effect")
    def druginfo_create_drug_effect(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return create_drug_effect(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return create_drug_effect(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_merge_drug_effect")
    def druginfo_merge_drug_effect(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return merge_drug_effect(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return merge_drug_effect(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_update_drug_effect")
    def druginfo_update_drug_effect(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return update_drug_effect(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return update_drug_effect(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_delete_drug_effect")
    def druginfo_delete_drug_effect(effectId: int, timeout: int = 15) -> Dict[str, Any]:
        try:
            return delete_drug_effect(effect_id=int(effectId), timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return delete_drug_effect(effect_id=int(effectId), timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_create_drug_kind")
    def druginfo_create_drug_kind(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return create_drug_kind(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return create_drug_kind(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_merge_drug_kind")
    def druginfo_merge_drug_kind(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return merge_drug_kind(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return merge_drug_kind(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_update_drug_kind")
    def druginfo_update_drug_kind(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return update_drug_kind(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return update_drug_kind(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_delete_drug_kind")
    def druginfo_delete_drug_kind(id: int, timeout: int = 15) -> Dict[str, Any]:
        try:
            return delete_drug_kind(effect_id=int(id), timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return delete_drug_kind(effect_id=int(id), timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_create_guide_a4")
    def druginfo_create_guide_a4(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return create_guide_a4(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return create_guide_a4(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_merge_guide_a4")
    def druginfo_merge_guide_a4(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return merge_guide_a4(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return merge_guide_a4(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_update_guide_a4")
    def druginfo_update_guide_a4(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return update_guide_a4(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return update_guide_a4(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_delete_guide_a4")
    def druginfo_delete_guide_a4(id: int, timeout: int = 15) -> Dict[str, Any]:
        try:
            return delete_guide_a4(guide_id=int(id), timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return delete_guide_a4(guide_id=int(id), timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_create_guide_a5")
    def druginfo_create_guide_a5(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return create_guide_a5(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return create_guide_a5(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_merge_guide_a5")
    def druginfo_merge_guide_a5(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return merge_guide_a5(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return merge_guide_a5(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_update_guide_a5")
    def druginfo_update_guide_a5(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return update_guide_a5(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return update_guide_a5(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_delete_guide_a5")
    def druginfo_delete_guide_a5(id: int, timeout: int = 15) -> Dict[str, Any]:
        try:
            return delete_guide_a5(guide_id=int(id), timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return delete_guide_a5(guide_id=int(id), timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_create_main_ingredient")
    def druginfo_create_main_ingredient(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return create_main_ingredient(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return create_main_ingredient(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_bulk_main_ingredient")
    def druginfo_bulk_main_ingredient(code: str, body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return bulk_main_ingredient(code=code, body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return bulk_main_ingredient(code=code, body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_update_main_ingredient")
    def druginfo_update_main_ingredient(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return update_main_ingredient(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return update_main_ingredient(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_delete_main_ingredient")
    def druginfo_delete_main_ingredient(code: str, timeout: int = 15) -> Dict[str, Any]:
        try:
            return delete_main_ingredient(code=code, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return delete_main_ingredient(code=code, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_delete_main_ingredient_cache")
    def druginfo_delete_main_ingredient_cache(code: str, timeout: int = 15) -> Dict[str, Any]:
        try:
            return delete_main_ingredient_cache(code=code, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return delete_main_ingredient_cache(code=code, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_update_main_ingredient_picto")
    def druginfo_update_main_ingredient_picto(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return update_main_ingredient_picto(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return update_main_ingredient_picto(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_create_product")
    def druginfo_create_product(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return create_product(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return create_product(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_update_product")
    def druginfo_update_product(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 15) -> Dict[str, Any]:
        try:
            return update_product(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return update_product(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_export_product")
    def druginfo_export_product(body: Dict[str, Any], contentType: Optional[str] = None, timeout: int = 30) -> Dict[str, Any]:
        try:
            return export_product(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except UnauthorizedError:
            _try_auto_login(timeout)
            return export_product(body=body, timeout=int(timeout), content_type=contentType or "application/json")
        except DrugInfoError as e:
            raise RuntimeError(str(e))

    @mcp.tool(name="druginfo_delete_product")
    def druginfo_delete_product(code: str, timeout: int = 15) -> Dict[str, Any]:
        try:
            return delete_product(code=code, timeout=int(timeout))
        except UnauthorizedError:
            _try_auto_login(timeout)
            return delete_product(code=code, timeout=int(timeout))
        except DrugInfoError as e:
            raise RuntimeError(str(e))

