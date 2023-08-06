from django import forms
from django.contrib import admin

from mentions.models import (
    HCard,
    OutgoingWebmentionStatus,
    PendingIncomingWebmention,
    PendingOutgoingContent,
    SimpleMention,
    Webmention,
)
from mentions.models.managers.webmention import WebmentionQuerySet

RETRYABLEMIXIN_FIELDS = [
    "is_awaiting_retry",
    "last_retry_attempt",
    "retry_attempt_count",
]


@admin.action(permissions=["change"])
def mark_webmention_approved(modeladmin, request, queryset: WebmentionQuerySet):
    queryset.mark_as_approved()


@admin.action(permissions=["change"])
def mark_webmention_unapproved(modeladmin, request, queryset: WebmentionQuerySet):
    queryset.mark_as_unapproved()


@admin.action(permissions=["change"])
def mark_webmention_read(modeladmin, request, queryset: WebmentionQuerySet):
    queryset.mark_as_read()


@admin.action(permissions=["change"])
def mark_webmention_unread(modeladmin, request, queryset: WebmentionQuerySet):
    queryset.mark_as_unread()


class BaseAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(SimpleMention)
class QuotableAdmin(BaseAdmin):
    list_display = [
        "source_url",
        "target_url",
        "hcard",
    ]
    search_fields = [
        "source_url",
        "target_url",
        "hcard",
    ]
    readonly_fields = [
        "target_object",
        "published",
    ]
    date_hierarchy = "published"


class WebmentionModelForm(forms.ModelForm):
    class Meta:
        model = Webmention
        widgets = {
            "quote": forms.Textarea(attrs={"rows": 3}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }
        fields = "__all__"


@admin.register(Webmention)
class WebmentionAdmin(QuotableAdmin):
    form = WebmentionModelForm
    readonly_fields = QuotableAdmin.readonly_fields + [
        "content_type",
        "object_id",
    ]
    actions = [
        mark_webmention_approved,
        mark_webmention_unapproved,
        mark_webmention_read,
        mark_webmention_unread,
    ]
    list_display = [
        "source_url",
        "target_url",
        "has_been_read",
        "published",
        "validated",
        "approved",
        "target_object",
    ]
    fieldsets = (
        (
            "Remote source",
            {
                "fields": (
                    "source_url",
                    "sent_by",
                    "hcard",
                    "quote",
                    "post_type",
                ),
            },
        ),
        (
            "Local target",
            {
                "fields": (
                    "target_url",
                    "content_type",
                    "object_id",
                    "target_object",
                ),
            },
        ),
        (
            "Metadata",
            {
                "fields": (
                    "published",
                    "has_been_read",
                    "approved",
                    "validated",
                    "notes",
                ),
            },
        ),
    )


@admin.register(OutgoingWebmentionStatus)
class OutgoingWebmentionStatusAdmin(BaseAdmin):
    readonly_fields = [
        "created_at",
        "source_url",
        "target_url",
        "target_webmention_endpoint",
        "status_message",
        "response_code",
        "successful",
        *RETRYABLEMIXIN_FIELDS,
    ]
    list_display = [
        "source_url",
        "target_url",
        "successful",
        "created_at",
    ]
    date_hierarchy = "created_at"


@admin.register(HCard)
class HCardAdmin(BaseAdmin):
    list_display = ["name", "homepage"]
    search_fields = ["name", "homepage"]


@admin.register(PendingIncomingWebmention)
class PendingIncomingAdmin(BaseAdmin):
    readonly_fields = [
        "created_at",
        "source_url",
        "target_url",
        "sent_by",
        *RETRYABLEMIXIN_FIELDS,
    ]


@admin.register(PendingOutgoingContent)
class PendingOutgoingAdmin(BaseAdmin):
    readonly_fields = [
        "created_at",
        "absolute_url",
        "text",
    ]
